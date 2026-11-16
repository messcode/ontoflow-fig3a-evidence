# Fig. 3A natural-analysis full result board, six-arm v1

Each harness used deepseek-flash on the same 24 scientific cases with two repetitions. The primary outcome requires both the scientific decision and the evidence or numerical result to pass. Each row includes all 48 scheduled slots. Missing submissions count as zero.

| Harness | Submitted | Decision correct | Evidence correct | Joint pass | Rate | Model calls |
|---|---:|---:|---:|---:|---:|---:|
| [Codex](scores/FR24-natural-6a2482caea42-codex-I-616c95764359/manifest.json) | 46 | 43 | 42 | 42/48 | 87.5% | 510 |
| [Claude Code](scores/FR24-natural-6a2482caea42-claude-I-616c95764359/manifest.json) | 47 | 45 | 42 | 41/48 | 85.4% | 1,048 |
| [Biomni](scores/FR24-natural-6a2482caea42-biomni-I-616c95764359/manifest.json) | 48 | 42 | 40 | 39/48 | 81.2% | 931 |
| [CellVoyager](scores/FR24-natural-6a2482caea42-cellvoyager-I-616c95764359/manifest.json) | 47 | 44 | 40 | 40/48 | 83.3% | 1,006 |
| [Codex + OntoFlow](scores/FR24-natural-6a2482caea42-codex-ontoflow-I-616c95764359/manifest.json) | 48 | 45 | 44 | 44/48 | 91.7% | 932 |
| [Claude Code + OntoFlow](scores/FR24-natural-0c735f4c9fc6-claude-ontoflow-I-bc39114794e4/manifest.json) | 48 | 43 | 44 | 42/48 | 87.5% | 1,406 |
| **Total** | 284 | 262 | 252 | **248/288** | **86.1%** | 5,833 |

The five existing rows retain the frozen #133 verdicts. The sixth row is a later single-arm extension using the original catalog, native Claude Code binary, scientific reader, resource limits and scoring rubric. Both masked first passes use deepseek-flash. The extension uses tool-free Qwen3-30B-A3B-Instruct-2507 for disagreement and sampled-agreement arbitration. The original panel used GPT-6. All results describe development cases. [Original results](https://github.com/messcode/Ontoflow/pull/133) · [Claude adapter qualification](https://github.com/messcode/Ontoflow/pull/135)

[Shared roster](roster.json) · [Aggregate measures](summary.json)
