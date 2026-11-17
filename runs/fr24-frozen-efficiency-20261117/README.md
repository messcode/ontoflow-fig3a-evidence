# FR24 frozen harness efficiency comparison

Two repetitions per harness on each of 24 development tasks. Each score manifest carries the case and input revision, cohort, guide and answer digests, scientific decision and evidence verdicts, and provider-reported usage for all 48 cells. Cached input is included in input tokens. Grading usage is excluded.

| Score manifest | Joint passes | Calls | Total tokens | Manifest SHA-256 |
|---|---:|---:|---:|---|
| [candidate](scores/FR24-efficiency-98254d0dcba3-candidate-I-8ecd3f148a84/manifest.json) | 44/48 | 998 | 20,699,935 | `79fb08ae9f5f0b1fecd6644a2c216be72a2e78d1b9b97d0551e212b022009f64` |
| [catalog-v2](scores/FR24-efficiency-98254d0dcba3-catalog-v2-I-8ecd3f148a84/manifest.json) | 40/48 | 1,306 | 27,345,870 | `6aa8fd76ba46db08f80f40a8f7c57cdbf747509194fbea8c58f32b3e9c98370b` |

The pilot contributed 12 cells per harness and the extension contributed 36. Each row retains its original cohort and sealed answer digest. The cohort verdict digests identify the two original score revisions. The paired comparison saved 6,645,935 tokens (24.3%). All 96 cells submitted.

The [run roster](roster.json) identifies the common cells. The [provenance record](provenance.json) identifies the original run freezes, scientific verdict seals, reference digests, and the post-run source commit that reproduces the frozen harness. Detailed scientific answers and blind-review materials remain in their controlled archives.
