# Fig. 3A paired Qwen3-30B-A3B results after the multi-tool context repair

| Harness | Submitted | Decision | Evidence | Joint | Input tokens | Generated tokens | Total tokens | Tool calls | Executed commands |
|---|---|---|---|---|---|---|---|---|---|
| Native Codex + boundary compiler | 35 | 6 | 0 | 0/48 (0.0%) | 45,589,065 | 383,124 | 45,972,189 | 3105 | 3101 |
| Plain native Codex | 30 | 4 | 3 | 3/48 (6.2%) | ≥50,191,995 | ≥409,728 | ≥50,601,723 | 3564 | 3496 |

Across the 48 matched pairs, 0 passed in both arms, 3 only with plain Codex, 0 only with the boundary compiler and 45 in neither. A missing submission counts as a failed joint check. Scientific token totals include compaction and truncated generation. Grading usage is excluded.

## Multi-tool replay and full-run checks

The previous MO-04 plain compaction request in repetition two contained 33,709 input tokens. The repaired transport retained the native headers and both ends of four long tool outputs. H200 measured 19,592 tokens and returned a completed summary. Separate native plain and boundary clients each executed four wide reads, compacted the resulting history on H200 and received the subsequent engineering completion.

| Arm | Metered requests | Requests shortened | Cells affected | Raw prompts ≥32,768 | Outputs shortened | Provider rejections |
|---|---|---|---|---|---|---|
| Plain native Codex | 4011 | 7 | 2 | 0 | 14 | 0 |
| Native Codex + boundary compiler | 3576 | 7 | 4 | 0 | 14 | 0 |

Both arms reserved the full per-request generation allowance before inference. The transport used the deployed model template and tokenizer to count the entire request. When needed, it shortened only native tool output bodies and labeled the omitted middle. The original tool results and their status remained in the host records. The protocol permits the model to issue a narrower follow-up query if a needed value was omitted.

The H200 service disconnected during DE-04 plain, repetition one, after processing its 14,808-token prompt. The model had already generated 4,931 tokens in this cell. The last request returned no usage receipt. The submitted-answer count excludes this missing answer, the denominator includes it, and the plain arm's scientific token and generated tool-call totals are lower bounds. The pinned service was restarted and the schedule resumed with the next cell.

## Measurement and scoring

All 96 measurements were fresh. Each arm ran the same 24 FR24 development cases twice with matched packet bytes, seeds, Q8_0 weights on H200, native Codex binary, tool descriptions and 3,600-second wall limit. The 32,768-token inference window, 16,000-token compaction trigger, per-request ceiling of 8,192 generated tokens and per-cell ceiling of 16,384 were retained. Scientific commands ran on gpu72. The engineering replay and all previous scientific submissions are excluded. The roster has prior development exposure.

Two blinded DeepSeek Flash first passes reviewed the sealed submissions. GPT-6.2 Astra Batch adjudicated 11 disputed ballots and 5 sampled agreements. It changed at least one field on 1 sampled agreements. The scientific measurements took 5.52 hours of elapsed wall time. Blinded review took 0.07 hours.

The previous full cohort recorded 1/48 joint passes for plain Codex and 2/48 for boundary. Its missing submissions included one provider context rejection. The development cases and sampling procedure were reused across cohorts. Changes in scientific scores cannot be attributed solely to that single rejected request.

[Plain native Codex manifest](scores/FR24-qwen30b-50f7dabc2b2d-plain-I-astra62-dbbbd7b67eae/manifest.json) · [Native Codex + boundary compiler manifest](scores/FR24-qwen30b-50f7dabc2b2d-boundary-I-astra62-dbbbd7b67eae/manifest.json) · [Paired roster](roster.json) · [Context receipts](context-audit.json) · [Review and usage summary](summary.json)
