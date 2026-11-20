"""Narrow compatibility fixes for the pinned local Qwen3 scientific evaluation."""
from copy import deepcopy
import hashlib

TEMPLATE_SHA256 = "57f1fd00f0013a2be96aa79b857391f27e23df5b5f847072b524c897e24d0361"
ASSISTANT_CONTENT = "{%- set content = message.content %}"


def renderable_template(source):
    """Keep literal text intact when converting a tool-only assistant message."""
    if hashlib.sha256(source.encode()).hexdigest() != TEMPLATE_SHA256:
        raise ValueError("Unexpected Qwen3 GGUF template")
    return source.replace(
        ASSISTANT_CONTENT,
        "{%- set content = message.content if message.content is not none else '' %}",
    ).replace("if '</think>' in message.content", "if '</think>' in content")


def local_tools(tools, *, approval_policy):
    """Expose supported native arguments without editing model-returned commands."""
    if approval_policy != "never":
        return tools
    result = deepcopy(tools)
    for tool in result:
        function = tool.get("function", {})
        if function.get("name") == "exec_command":
            props = function["parameters"]["properties"]
            for name in ("sandbox_permissions", "justification", "prefix_rule"):
                props.pop(name, None)
            function["description"] += (
                " Use the configured default permissions. Reading /input is available "
                "with an ordinary command. Supply cmd and omit approval-related fields."
                " For multi-step Python calculations, use a single quoted shell heredoc"
                " with real line breaks, in this form:\n"
                "/opt/science/bin/science-python - <<'PY'\nprint('example')\nPY\n"
                "Replace the example body with your calculation and explicit print calls"
                " for the requested results and records. In a one-line Python -c program,"
                " # comments out the rest of the line. If a calculation returns no text,"
                " correct the program before retrying. Once the results are printed,"
                " use them to answer."
            )
    return result


def output_allowance(used, budget, per_request):
    if used < 0 or budget <= 0 or per_request <= 0 or used > budget:
        raise ValueError("Invalid generation budget or receipt")
    return min(per_request, budget - used)
