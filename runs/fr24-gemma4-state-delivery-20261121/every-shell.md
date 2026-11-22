# Prior FR24 Gemma 4 26B every-shell state delivery pilot

This earlier cohort ran the same six development cases, with a separate concurrent Passive control. Active supplied a state snapshot at each eligible shell result and logged 55 deliveries.

| Arm | Submitted | Joint pass | Input tokens | Output tokens | Total tokens |
|---|---:|---:|---:|---:|---:|
| Passive | 6/6 | 3/6 | 743,072 | 70,682 | 813,754 |
| Active | 5/6 | 1/6 | 739,683 | 102,486 | 842,169 |

| Case | Passive | Active | Passive tokens | Active tokens |
|---|---|---|---:|---:|
| DE-02 | Joint pass | Evidence failed | 96,659 | 77,666 |
| MO-01 | Joint pass | Decision and evidence failed | 159,608 | 83,931 |
| RV-04 | Evidence failed | Decision failed | 94,805 | 320,710 |
| SC-01 | Evidence failed | Decision and evidence failed | 165,362 | 89,478 |
| SV-04 | Joint pass | Joint pass | 185,726 | 192,176 |
| VA-03 | Evidence failed | No submission (per-request output limit) | 111,594 | 78,208 |

The score contains two DeepSeek Flash first passes and four GPT-6.2 Astra Batch dispute verdicts. Missing submissions count as joint failures. Tokens include truncated completions.

[Earlier per-cell records and trace hashes](every-shell.json) · [Review and archive hashes](provenance.json) · [Event-triggered pilot](README.md)
