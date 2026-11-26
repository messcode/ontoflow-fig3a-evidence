# Fig. 3A FR24 Artifact-Boundary v1.3.1 Compact-Delivery Paired Results (`2026-11-26`)

Fresh 96-cell paired FR24 development cohort (`24 cases × 2 repetitions × 2 arms`, schedule seed `3411`, `12` workers) comparing symmetric `Plain native Codex` against `Native Codex + boundary compiler (v1.3.1 compact)` (`ArtifactBoundaryCompiler` with host-only `status_dir` + `ReadAwareStateDelivery(..., compact_view=True)` over `/v1/responses`, zero `/workspace/.ontoflow` mounts). Both arms used `deepseek-flash`, identical developer instructions (`frozen.GUIDE`), a `32,000`-token native compaction threshold, and a `900`-second wall ceiling.

| Arm | Submitted | Decision | Evidence | Joint | Model calls | Cached input | Uncached input | Output | Provider tokens |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Native Codex + boundary compiler (v1.3.1 compact) | 48 | 46 | 44 | **44/48** | 651 | 10,504,448 | 1,183,749 | 935,137 | **12,623,334** |
| Plain native Codex | 47 | 42 | 41 | 41/48 | 808 | 13,382,656 | 1,479,504 | 1,119,750 | 15,981,910 |

Provider token counts cover `1,459 / 1,459` numbered scientific requests (`0` missing usage receipts) and exclude grading. Across the `48` matched pairs, both arms passed `41`, only `boundary` passed `3` (`SC-01` rep 2, `SC-03` rep 2, `VA-04` rep 1), only `plain` passed `0`, and neither passed `4` (`MO-04` reps 1–2, `VA-01` reps 1–2).

Two blinded tool-free DeepSeek Flash first passes and one `gpt-6.2-astra` Batch adjudication (`13` disputed ballots + `9` presampled agreements = `22` requests, `1` audit change) used the frozen FR24 reference protocol.

[Frozen roster](roster.json) · [Provenance](provenance.json)

- [boundary score and receipt digests](scores/FR24-boundary-1b09d9797608-boundary-I-89438b9af950/manifest.json)
- [plain score and receipt digests](scores/FR24-boundary-341faad49250-plain-I-89438b9af950/manifest.json)
