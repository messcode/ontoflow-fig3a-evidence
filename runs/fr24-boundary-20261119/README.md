# FR24 artifact boundary versus plain native Codex · 19 November 2026

The boundary arm earned 42/48 joint scientific passes (87.5%) and the concurrent plain arm earned 38/48 (79.2%). The boundary arm used 875,989 fewer reported provider tokens (6.4% relative to plain).

| Arm | Submitted / 48 | Decision / 48 | Evidence / 48 | Joint / 48 | Requests | Cached input | Uncached input | Output | Total tokens |
|---|---|---|---|---|---|---|---|---|---|
| Plain native Codex | 47 | 42 | 38 | 38 | 693 | 11,163,904 | 1,521,478 | 1,025,438 | 13,710,820 |
| Native Codex + boundary compiler | 48 | 44 | 42 | 42 | 674 | 10,949,120 | 1,061,142 | 824,569 | 12,834,831 |

Across the 48 matched case–repetition pairs, both arms passed 38, only boundary passed 4, only plain passed 0, and both missed 6. The four boundary-only passes were MO-02 replicate 2, SC-03 replicate 2 and both VA-03 repetitions. A joint pass requires both the correct scientific decision and the requested supporting evidence in the same submission.

Two independent, tool-free DeepSeek Flash review passes received masked answers and frozen scientific references. A separate Qwen3-30B-A3B-Instruct-2507 reviewer adjudicated 11 disputed ballots and independently rechecked 10 presampled agreements. All 10 sampled agreements stood. The host sealed scientific verdicts before joining the arm key.

Provider receipts covered 1,367/1,367 numbered scientific model requests. Cached input is included once. Counts span each attempt through its endpoint and exclude grading and the six qualification pilots. The transport logs recorded no retries.

These 24 cases have prior development exposure. The comparison measures the compiler and its visible workspace summary together, with two fresh draws per case and arm.

## Score manifests

- [Native Codex + boundary compiler](scores/FR24-boundary-2d70bf57261e-boundary-I-0a1e9dcb73ca/manifest.json) · SHA-256 `078e806ed4d8ed21cd9052c0b7a9c393ba98201e35be5b28afc4e09d8045f2de`
- [Plain native Codex](scores/FR24-boundary-773da31839aa-plain-I-0a1e9dcb73ca/manifest.json) · SHA-256 `69866ad8825e8adebc9a3a56503c1f873f4790ba5f651dd83f4ddaa5f5261633`

Restricting descriptively to the 47 pairs in which both arms submitted gives 41/47 boundary and 38/47 plain joint passes, with 12,563,809 and 13,511,799 tokens respectively. The one missing submission was plain SC-03 replicate 2 after a local request-size rejection.

The [planned roster](roster.json) binds each case and repetition to the delivered input revision. The [provenance receipt](provenance.json) identifies the measured runtime, scientific references, reviewer version, answer assignment digest and adjudication seal. The per-cell manifests include scientific fields, answer digests and usage for every planned slot.
