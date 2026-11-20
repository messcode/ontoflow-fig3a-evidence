# Fig. 3A · Qwen3-30B-A3B with native Codex and the boundary compiler

| Qwen3-30B-A3B Q8_0 | Submitted | Decision | Evidence | Joint | Model requests | Input tokens | Output tokens | Total tokens | Executed commands |
|---|---|---|---|---|---|---|---|---|---|
| Native Codex + boundary compiler | 30 | 6 | 2 | 2/48 | 3,651 | 45,937,798 | 403,913 | 46,341,711 | 3187 |
| Plain native Codex | 34 | 6 | 1 | 1/48 | 3,303 | 41,169,999 | 372,710 | 41,542,709 | 2910 |

Boundary used 4,799,002 more scientific tokens (+11.6%) and submitted four fewer answers. Of 48 matched pairs, 0 passed in both arms, 2 passed only with the boundary compiler, 1 passed only with plain native Codex and 45 passed in neither. A joint pass requires both the scientific judgment and its evidence. Missing submissions count as zero joint passes.

| Family | Plain submitted | Plain joint | Boundary submitted | Boundary joint |
|---|---|---|---|---|
| DE | 6/8 | 0/8 | 6/8 | 0/8 |
| MO | 5/8 | 0/8 | 2/8 | 0/8 |
| RV | 8/8 | 0/8 | 8/8 | 1/8 |
| SC | 6/8 | 0/8 | 5/8 | 0/8 |
| SV | 3/8 | 0/8 | 2/8 | 0/8 |
| VA | 6/8 | 1/8 | 7/8 | 1/8 |

## Submission failures and scientific errors

| Arm | All missing submissions | Context overflow (within missing) | Other missing submissions | Submitted answers failing scientific review | Joint passes |
|---|---|---|---|---|---|
| Native Codex + boundary compiler | 18 | 0 | 18 | 28 | 2 |
| Plain native Codex | 14 | 1 | 13 | 33 | 1 |

The service rejected over-window requests in 1 cells (MO-04 plain (rep 2)). The archived compaction request for MO-04 plain, repetition two, shows how this happened. After consecutive requests for wide table headers, the service received 33,709 input tokens against its 32,768-token context window. The agent had generated 6,234 tokens before the rejection. The run paused between cells after the 60th result was sealed and resumed from the original process. This missing submission contributes one joint failure. The other 31 missing submissions ended with a truncated completion. Thirty used the full 16,384 generated tokens. SC-03 plain in repetition two reached its 8,192-token single-request limit after using 16,329 tokens across the cell. The scientific fields for missing answers are null. A submitted answer fails joint review when either its decision or its supporting evidence fails.

## Run and review

The two arms each ran two fresh repetitions on all 24 frozen FR24 development cases. One H200 served Qwen3-30B-A3B Q8_0, with native commands executed on the separate tool host. The cell fixtures, native binary, scientific container, runner and compiler matched the frozen boundary cohort. Both arms used full native tool results and the same multiline Python tool description. The boundary arm additionally had the artifact compiler and its workspace summary.

Every cell used a cleared inference slot, thinking disabled, temperature 0.7, top-p 0.8 and top-k 20. Each repetition used matched request seeds across arms, starting at 3412 and 13412 respectively. The generated-token budget was 16,384 per cell, with 8,192 per request and a 3,600-second wall limit. A pilot compaction request exceeded the 32,768-token window. Lowering the automatic compaction trigger from 24,000 to 16,000 preserved the window and generation budget. Long-output engineering replays passed in both arms. All pilot and engineering trials are excluded.

The frozen scientific reviewer used two independent blinded DeepSeek Flash passes per submission. GPT-6.2 Astra Batch reviewed the disputed scientific fields for 7 ballots and both fields for 5 presampled agreement ballots. It changed at least one field on 0 sampled agreements. Answers and scoring fields were sealed before unblinding. Token totals sum all scientific input and generated tokens for metered inference responses, including compaction and truncated responses. Model requests also count any rejected requests. Evaluation usage is excluded.

The 24 cases have prior development exposure. The historical DeepSeek rows use a different model, tokenizer and budget. The paired contrast within this study uses the same model and budget in both arms.

[Native Codex + boundary compiler manifest](scores/FR24-qwen30b-4196b0469a56-boundary-I-astra62-148250c38796/manifest.json) · [Plain native Codex manifest](scores/FR24-qwen30b-4196b0469a56-plain-I-astra62-148250c38796/manifest.json) · [Roster](roster.json) · [Provenance and seal digests](summary.json)
