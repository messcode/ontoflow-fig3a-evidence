# FR24 Gemma 4 26B event-triggered state delivery pilot

Partial development ablation of six original FR24 cases, one attempt per case and arm. All 12 planned cells were sealed. This covers six of 24 FR24 cases and six of 48 reference slots per arm. Joint passes use six as the denominator and require a correct decision and decisive evidence. Missing submissions count as joint failures.

Both arms used native Codex with the same boundary compiler and read-only inputs. Passive had the original file path and reminder. Active received the full state at the first eligible shell reply, a delta for a changed artifact record and one full refresh after native context compaction. Injected text was transient and counted in the original context budget.

| Arm | Submitted | Joint pass | Input tokens | Output tokens | Total tokens |
|---|---:|---:|---:|---:|---:|
| Passive | 5/6 | 1/6 | 807,823 | 86,933 | 894,756 |
| Active | 5/6 | 2/6 | 831,426 | 97,829 | 929,255 |

| Case | Passive | Active | Passive tokens | Active tokens |
|---|---|---|---:|---:|
| DE-02 | Joint pass | Evidence failed | 95,782 | 152,634 |
| MO-01 | No submission (per-request output limit) | Joint pass | 166,244 | 181,402 |
| RV-04 | Decision failed | Joint pass | 122,138 | 145,060 |
| SC-01 | Decision and evidence failed | Decision and evidence failed | 184,849 | 212,166 |
| SV-04 | Decision and evidence failed | No submission (per-request output limit) | 169,983 | 121,971 |
| VA-03 | Evidence failed | Evidence failed | 155,760 | 116,022 |

Active confirmed six initial deliveries and skipped 51 unchanged states. Artifact changes and post-compaction refresh each triggered zero deliveries in these trajectories. Two DeepSeek Flash passes were preserved. GPT-6.2 Astra Batch returned four dispute verdicts and one audit verdict. Tokens come from scientific provider receipts and include the two truncated completions.

## Evidence

- [Passive score manifest](scores/FR24-gemma4-26b-state-event-20261121-passive-I-astra62-71dd32ce4926/manifest.json) · SHA-256 `1e38552a997a0f4bd9b6613f9ffed6635f926fb7458752b9ea1f451f977803eb`
- [Active score manifest](scores/FR24-gemma4-26b-state-event-20261121-active-I-astra62-71dd32ce4926/manifest.json) · SHA-256 `a922c8559c195ed8323223b3b195afe88c673ca91bfe579e5f9df9fa526962eb`
- [Six-case roster](roster.json) and [manifest checksums](manifests.json)
- [Run settings, prompt and injection hashes, and review seals](provenance.json)
- [Prior every-shell injection comparison](every-shell.md)

The archived private evidence contains per-turn traces, tool output, answers and ballots. The files here carry outcomes and digests for verification. Preserve each run's own Passive comparison.
