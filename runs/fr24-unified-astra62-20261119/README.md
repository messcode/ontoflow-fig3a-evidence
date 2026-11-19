# FR24 unified GPT-6.2 Astra arbitration

A single GPT-6.2 Astra Batch adjudicated 49 disputed ballots and 51 presampled agreements across 11 FR24 development arms. Both original DeepSeek Flash passes were retained. All 100 requests returned a valid verdict. The scientific runs, 522 submitted answers and six missing slots retain their original identities and token counts.

The boundary compiler passed 43/48 and concurrent plain Codex passed 42/48. Of 48 matched pairs, 40 passed in both arms, three only with the boundary, two only with plain Codex and three in neither. Both arms passed 42 of the 47 pairs where both submitted. The 875,989-token saving (6.4%) is unchanged.

| Cohort | Harness | Decision, prior → new | Evidence, prior → new | Joint, prior → new | Joint change |
|---|---|---:|---:|---:|---:|
| #150 | Native Codex + boundary compiler | 44 → 43 | 42 → 44 | 42 → 43 | +1 |
| #150 | Plain native Codex | 42 → 42 | 38 → 43 | 38 → 42 | +4 |
| #142 | Frozen OntoFlow candidate | 45 → 47 | 45 → 43 | 44 → 43 | -1 |
| #142 | Catalog v2 control | 43 → 44 | 40 → 43 | 40 → 41 | +1 |
| Historical | Codex + OntoFlow (original) | 45 → 45 | 44 → 44 | 44 → 44 | +0 |
| Historical | Codex + OntoFlow catalog v2 | 44 → 45 | 44 → 42 | 44 → 42 | -2 |
| Historical | Claude Code + OntoFlow | 43 → 47 | 44 → 44 | 42 → 44 | +2 |
| Historical | Codex | 43 → 43 | 42 → 42 | 42 → 42 | +0 |
| Historical | Claude Code | 45 → 45 | 42 → 42 | 41 → 41 | +0 |
| Historical | CellVoyager | 44 → 44 | 40 → 40 | 40 → 40 | +0 |
| Historical | Biomni | 42 → 42 | 40 → 37 | 39 → 37 | -2 |

The 100 requests were randomly ordered and independently evaluated with anonymous IDs, no tools and the frozen scientific reference. Disputes exposed the two original scientific reviews and requested only the disputed fields. Sampled agreements hid both original votes and requested both fields. Historical calibration duplicates were excluded. The host validated each response and sealed the output digest before joining the private arm mapping. An independent replay checked all 528 slots against the original archive ballots.

Relative to the previously published verdicts, 33 slots changed at least one scientific field. Fourteen joint failures became passes, eleven passes became failures, and eight retained a joint failure. Of the 33 changed slots, 22 came from disagreements and 11 from sampled agreements. Compared directly with the agreeing DeepSeek first passes, Astra changed at least one field on 12 of the 51 audited answers. Earning a joint pass requires both fields.

The 100 provider receipts total 183,558 input tokens (44,786 ordinary input and 138,772 short-lived cache writes) and 16,433 output tokens including 3,876 reasoning tokens. There were zero cache reads and zero 12-hour cache writes. Batch pricing of $4, $5 and $20 per million ordinary input, 30-minute cache-write and output tokens gives **US$1.201664** ($1.20 rounded). Reasoning tokens are included once. These grading tokens are excluded from all scientific-run totals. [API pricing](https://developers.openai.com/api/docs/pricing)

The [summary and change list](summary.json) binds the six previous review seals to the new input and output digests. Each score manifest references its predecessor and retains the original scientific-run slots.

- [Native Codex + boundary compiler, #150](scores/FR24-boundary-2d70bf57261e-boundary-I-astra62-a3d40000ba61/manifest.json)
- [Plain native Codex, #150](scores/FR24-boundary-773da31839aa-plain-I-astra62-a3d40000ba61/manifest.json)
- [Frozen OntoFlow candidate, #142](scores/FR24-efficiency-98254d0dcba3-candidate-I-astra62-a3d40000ba61/manifest.json)
- [Catalog v2 control, #142](scores/FR24-efficiency-98254d0dcba3-catalog-v2-I-astra62-a3d40000ba61/manifest.json)
- [Codex + OntoFlow (original), Historical](scores/FR24-natural-6a2482caea42-codex-ontoflow-I-astra62-a3d40000ba61/manifest.json)
- [Codex + OntoFlow catalog v2, Historical](scores/FR24-natural-561f562db646-codex-ontoflow-v2-I-astra62-a3d40000ba61/manifest.json)
- [Claude Code + OntoFlow, Historical](scores/FR24-natural-0c735f4c9fc6-claude-ontoflow-I-astra62-a3d40000ba61/manifest.json)
- [Codex, Historical](scores/FR24-natural-6a2482caea42-codex-I-astra62-a3d40000ba61/manifest.json)
- [Claude Code, Historical](scores/FR24-natural-6a2482caea42-claude-I-astra62-a3d40000ba61/manifest.json)
- [CellVoyager, Historical](scores/FR24-natural-6a2482caea42-cellvoyager-I-astra62-a3d40000ba61/manifest.json)
- [Biomni, Historical](scores/FR24-natural-6a2482caea42-biomni-I-astra62-a3d40000ba61/manifest.json)
