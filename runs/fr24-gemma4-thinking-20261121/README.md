# Fig. 3A Gemma 4 thinking-enabled paired FR24 development results

Each model ran 24 frozen FR24 development cases twice per arm on its own H200 NVL. Plain and passive boundary shared the native Codex binary, underlying case files, tools, decoding and budgets within each model. The 192 planned slots include missing submissions. Joint scientific success requires the correct decision and decisive evidence.

| Model | Harness | Submitted | Decision | Evidence | Joint | Calls | Provider tokens |
|---|---|---:|---:|---:|---:|---:|---:|
| Gemma-4-26B-A4B-Q8_0-thinking | Native Codex + passive boundary | 33 | 23 | 16 | 15/48 | 708 | 12,262,377 |
| Gemma-4-26B-A4B-Q8_0-thinking | Plain native Codex | 32 | 23 | 17 | 17/48 | 666 | 11,049,350 |
| Gemma-4-12B-Q8_0-thinking | Native Codex + passive boundary | 25 | 12 | 5 | 5/48 | 420 | 6,965,011 |
| Gemma-4-12B-Q8_0-thinking | Plain native Codex | 19 | 7 | 2 | 2/48 | 533 | 9,529,890 |

Provider token counts include metered attempts that produced no sealed answer and exclude grading. A leading ≥ denotes a missing usage receipt.

| Model | Both passed | Boundary only | Plain only | Neither |
|---|---:|---:|---:|---:|
| 26B | 11 | 4 | 6 | 27 |
| 12B | 0 | 5 | 2 | 41 |

Both arms retain the same 48-slot denominator per model. See the per-cell manifests for coverage, termination, separate prompt and completion usage, and execution time.
The two measurements took 4.07 elapsed hours.

Two blinded DeepSeek Flash first passes and one GPT-6.2 Astra Batch adjudication used a common pinned protocol. The adjudicator received 28 disputed and 8 sampled or audit items.

[Frozen roster](roster.json) · [Provenance](provenance.json) · [Score and usage summary](summary.json)

- [12b-boundary score and receipt digests](scores/FR24-gemma4-12b-8e9299739053-boundary-I-astra62-95f93d645d55/manifest.json)
- [12b-plain score and receipt digests](scores/FR24-gemma4-12b-7e72d877fcef-plain-I-astra62-95f93d645d55/manifest.json)
- [26b-boundary score and receipt digests](scores/FR24-gemma4-26b-9041d63ca2a3-boundary-I-astra62-95f93d645d55/manifest.json)
- [26b-plain score and receipt digests](scores/FR24-gemma4-26b-7c7f4759734f-plain-I-astra62-95f93d645d55/manifest.json)
