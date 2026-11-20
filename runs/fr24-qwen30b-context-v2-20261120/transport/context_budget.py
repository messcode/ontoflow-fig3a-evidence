"""Fit native shell history to a finite local inference context."""

import hashlib
import re

# The native runner emits one of these delimiters after its status lines.
OUTPUT_HEADER = re.compile(r"^(?:[^\n]*\n){0,8}?(?:Final output|Output):\n")
MIN_BODY = 128


def digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def fit_tool_history(chat, count_tokens, window):
    """Reserve max_tokens. Keep native input immutable and audit each omission."""
    target = window - chat["max_tokens"]
    raw = count_tokens(chat)
    receipt = {"window": window, "input_limit": target, "raw_tokens": raw,
               "delivered_tokens": raw, "omissions": []}
    if raw <= target:
        return chat, receipt

    candidates = {}
    for index, message in enumerate(chat["messages"]):
        if message["role"] != "tool":
            continue
        text = message["content"]
        header = OUTPUT_HEADER.match(text)
        if header and len(text) - header.end() > MIN_BODY:
            candidates[index] = (text[:header.end()], text[header.end():])

    # Halve successively on the original strings. Always measure the final
    # rendered request, including the marker, system text and tool schemas.
    cap = max((len(body) for _, body in candidates.values()), default=0)
    while cap > MIN_BODY:
        cap = max(MIN_BODY, cap // 2)
        messages = list(chat["messages"])
        omissions = []
        for index, (header, body) in candidates.items():
            if len(body) <= cap:
                continue
            front = (cap + 1) // 2
            tail = cap - front
            omitted = len(body) - cap
            marker = f"\n[local adapter omitted {omitted} characters of tool output]\n"
            visible = header + body[:front] + marker + body[-tail:]
            original = messages[index]
            messages[index] = {**original, "content": visible}
            omissions.append({"index": index, "call_id": original["tool_call_id"],
                              "omitted_chars": omitted, "raw_sha256": digest(original["content"]),
                              "visible_sha256": digest(visible)})
        delivered = {**chat, "messages": messages}
        size = count_tokens(delivered)
        if size <= target:
            receipt.update(delivered_tokens=size, omissions=omissions)
            return delivered, receipt
    raise ValueError(f"Fixed history exceeds prompt budget (raw={raw}, limit={target})")
