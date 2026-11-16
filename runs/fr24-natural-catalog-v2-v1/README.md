# Fig. 3A natural-analysis board: six systems plus catalog v2

The new version is the 48-cell PR #136 catalog replication with the original nomination format. Scientific execution was not rerun. Historical six-arm verdicts remain immutable. All 48 scheduled slots count; missing submissions score zero.

| Harness / version | Submitted | Decision | Evidence | Joint | Calls |
|---|---:|---:|---:|---:|---:|
| Codex + OntoFlow (original) | 48 | 45 | 44 | 44/48 | 932 |
| Codex + OntoFlow catalog v2 | 47 | 44 | 44 | 44/48 | 860 |
| Claude Code + OntoFlow | 48 | 43 | 44 | 42/48 | 1,406 |
| Codex | 46 | 43 | 42 | 42/48 | 510 |
| Claude Code | 47 | 45 | 42 | 41/48 | 1,048 |
| CellVoyager | 47 | 44 | 40 | 40/48 | 1,006 |
| Biomni | 48 | 42 | 40 | 39/48 | 931 |

## Review identity and limits

The original digest-verified natural reviewer (`d81175d95a49b0aff083f95ff8a542819982f65993e4757b1baf4e983bfd0e81`) provided masking, two independent deepseek-flash first passes, all disputed scientific fields and the deterministic 10% agreement audit. Six anonymous historical Claude calibration answers were mixed in and excluded from the new score. Two disagreements and six agreement audits were independently adjudicated using the latest sixth-arm extension's unmodified tool-free Qwen3-30B-A3B-Instruct-2507 MLX program and snapshot `e9675aa3ca5f900ccef55267914466d55ab325fa`. Each item used a separate context; all six agreement audits were maintained. The original five-arm arbiter was GPT-6. Six calibration answers produced two changed joint decisions relative to the historical panel (DE-01.1 and SC-01.1); original scores are not replaced. This is development evidence, not an equivalence or scientific improvement claim.

The earlier single-reviewer 45/48 is not the new board score. The sealed new result is 44/48. There are two pass-to-fail and two fail-to-pass transitions from the original version; SC-03.2 is a retained infrastructure miss.

## Cost accounting

All 48 planned cells: calls 932 -> 860; reported input 28,420,476 -> 26,024,587; reported output 884,923 -> 802,014. Input includes cached tokens. Uncached input is essentially flat (1,224,444 -> 1,226,507); savings are concentrated in cached input. No monetary price is inferred. Native Codex has one request without usage, explicitly recorded in cells.json. Among 46 jointly submitted native/v2 cells, joint passes are 42 vs 43, and total reported tokens are 11,554,507 vs 26,007,802 (2.25x).

[Original immutable six-arm board](https://github.com/messcode/ontoflow-fig3a-evidence/blob/c7634f46336550ef65545869757bc3fbe613f3c5/runs/fr24-natural-six-arm-v1/README.md) · [Shared roster](roster.json) · [Summary and paired transitions](summary.json) · [Scientific/cost cells](cells.json) · [Review seal](review-seal.json) · [Provenance](provenance.json)

New score: `FR24-natural-561f562db646-codex-ontoflow-v2-I-786a1018a47b`. Private answers, identity keys, ballots, model requests and raw traces remain in the private archive.
