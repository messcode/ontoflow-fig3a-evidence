# Area 4 benchmark results

## fig3a


### fig3a · full-blind-B

#### Scientific full strict · deepseek-flash · Development

Roster `FB-15d228bf5dab` · Passes / planned slots.

| Arm | Independent | Repair | Fixed 0→1 | Regressed 1→0 | Paired | Scored |
| --- | --- | --- | --- | --- | --- | --- |
| biomni | 0/8 | 0/8 | 0 | 0 | 8 | 8 → 8 |
| claude | 1/8 | 3/8 | 2 | 0 | 8 | 8 → 8 |
| codex-query | 3/8 | 5/8 | 2 | 0 | 8 | 8 → 8 |
| codex-static | 1/8 | 4/8 | 4 | 1 | 8 | 8 → 8 |

**Per-slot scientific scores** · independent → repair; — = unattempted, null = unscored.

| Family | View | Replicate | biomni | claude | codex-query | codex-static |
| --- | --- | --- | --- | --- | --- | --- |
| RV-01 | view-1 | 1 | 0→0 | 1→1 | 0→0 | 0→1 |
| RV-01 | view-1 | 2 | 0→0 | 0→1 | 1→1 | 0→1 |
| RV-01 | view-2 | 1 | 0→0 | 0→1 | 1→1 | 0→0 |
| RV-01 | view-2 | 2 | 0→0 | 0→0 | 1→1 | 1→0 |
| VA-01 | view-3 | 1 | 0→0 | 0→0 | 0→0 | 0→1 |
| VA-01 | view-3 | 2 | 0→0 | 0→0 | 0→1 | 0→0 |
| VA-01 | view-4 | 1 | 0→0 | 0→0 | 0→1 | 0→0 |
| VA-01 | view-4 | 2 | 0→0 | 0→0 | 0→0 | 0→1 |

**Rubric checks** · independent → repair counts. Full strict requires all seven checks. Host end-to-end verification is a separate metric.

| Check | biomni | claude | codex-query | codex-static |
| --- | --- | --- | --- | --- |
| Submission schema | 8→8 | 8→8 | 8→8 | 8→8 |
| Registered operation | 1→2 | 4→4 | 5→5 | 8→8 |
| Required roles | 0→8 | 2→8 | 4→8 | 5→8 |
| Exact role set | 0→5 | 1→5 | 3→6 | 3→6 |
| File or explicit null | 0→1 | 1→4 | 4→7 | 3→5 |
| Decision | 4→4 | 5→6 | 6→8 | 6→8 |
| Evidence citations | 2→2 | 8→8 | 8→8 | 8→8 |

<details><summary>Score manifests and run conditions</summary>

Shared settings: `prompt=sha256:441dc8e3334edd0e46b38f4984dacec416165b1ad6f3a9c30b9605c37833cc41|budget=4+1+1,240s,native-output|replicates=1,2|feedback=sealed-only`

- [FB-6b93b6cc7356-biomni-I](https://raw.githubusercontent.com/messcode/ontoflow-fig3a-evidence/5a55e96c60f9cc694ad4c6120b90a5a24a240a43/runs/FB-6b93b6cc7356/scores/FB-6b93b6cc7356-biomni-I/manifest.json) · [run index](https://github.com/messcode/ontoflow-fig3a-evidence/blob/5a55e96c60f9cc694ad4c6120b90a5a24a240a43/runs/FB-6b93b6cc7356/README.md)
- [FB-6b93b6cc7356-biomni-R](https://raw.githubusercontent.com/messcode/ontoflow-fig3a-evidence/5a55e96c60f9cc694ad4c6120b90a5a24a240a43/runs/FB-6b93b6cc7356/scores/FB-6b93b6cc7356-biomni-R/manifest.json) · [run index](https://github.com/messcode/ontoflow-fig3a-evidence/blob/5a55e96c60f9cc694ad4c6120b90a5a24a240a43/runs/FB-6b93b6cc7356/README.md)
- [FB-6b93b6cc7356-claude-I](https://raw.githubusercontent.com/messcode/ontoflow-fig3a-evidence/5a55e96c60f9cc694ad4c6120b90a5a24a240a43/runs/FB-6b93b6cc7356/scores/FB-6b93b6cc7356-claude-I/manifest.json) · [run index](https://github.com/messcode/ontoflow-fig3a-evidence/blob/5a55e96c60f9cc694ad4c6120b90a5a24a240a43/runs/FB-6b93b6cc7356/README.md)
- [FB-6b93b6cc7356-claude-R](https://raw.githubusercontent.com/messcode/ontoflow-fig3a-evidence/5a55e96c60f9cc694ad4c6120b90a5a24a240a43/runs/FB-6b93b6cc7356/scores/FB-6b93b6cc7356-claude-R/manifest.json) · [run index](https://github.com/messcode/ontoflow-fig3a-evidence/blob/5a55e96c60f9cc694ad4c6120b90a5a24a240a43/runs/FB-6b93b6cc7356/README.md)
- [FB-6b93b6cc7356-codex-query-I](https://raw.githubusercontent.com/messcode/ontoflow-fig3a-evidence/5a55e96c60f9cc694ad4c6120b90a5a24a240a43/runs/FB-6b93b6cc7356/scores/FB-6b93b6cc7356-codex-query-I/manifest.json) · [run index](https://github.com/messcode/ontoflow-fig3a-evidence/blob/5a55e96c60f9cc694ad4c6120b90a5a24a240a43/runs/FB-6b93b6cc7356/README.md)
- [FB-6b93b6cc7356-codex-query-R](https://raw.githubusercontent.com/messcode/ontoflow-fig3a-evidence/5a55e96c60f9cc694ad4c6120b90a5a24a240a43/runs/FB-6b93b6cc7356/scores/FB-6b93b6cc7356-codex-query-R/manifest.json) · [run index](https://github.com/messcode/ontoflow-fig3a-evidence/blob/5a55e96c60f9cc694ad4c6120b90a5a24a240a43/runs/FB-6b93b6cc7356/README.md)
- [FB-6b93b6cc7356-codex-static-I](https://raw.githubusercontent.com/messcode/ontoflow-fig3a-evidence/5a55e96c60f9cc694ad4c6120b90a5a24a240a43/runs/FB-6b93b6cc7356/scores/FB-6b93b6cc7356-codex-static-I/manifest.json) · [run index](https://github.com/messcode/ontoflow-fig3a-evidence/blob/5a55e96c60f9cc694ad4c6120b90a5a24a240a43/runs/FB-6b93b6cc7356/README.md)
- [FB-6b93b6cc7356-codex-static-R](https://raw.githubusercontent.com/messcode/ontoflow-fig3a-evidence/5a55e96c60f9cc694ad4c6120b90a5a24a240a43/runs/FB-6b93b6cc7356/scores/FB-6b93b6cc7356-codex-static-R/manifest.json) · [run index](https://github.com/messcode/ontoflow-fig3a-evidence/blob/5a55e96c60f9cc694ad4c6120b90a5a24a240a43/runs/FB-6b93b6cc7356/README.md)

</details>


### fig3a · role-known

#### Compliant · deepseek-v4-flash · Development

Roster `fig3a-24case-sc02note-v1` · Passes / planned slots.

| Arm | Independent | Scored |
| --- | --- | --- |
| biomni_staged_only | 36/96 | 96 |
| claude_code_no_surface | 53/96 | 96 |
| codex_no_surface | 48/96 | 96 |
| codex_with_surface | 60/96 | 96 |

**Passes by reporting group**

| Arm | A | B | C | D | E | F |
| --- | --- | --- | --- | --- | --- | --- |
| biomni_staged_only | 7/16 | 8/16 | 6/16 | 5/16 | 5/16 | 5/16 |
| claude_code_no_surface | 7/16 | 7/16 | 10/16 | 11/16 | 6/16 | 12/16 |
| codex_no_surface | 5/16 | 6/16 | 12/16 | 8/16 | 5/16 | 12/16 |
| codex_with_surface | 7/16 | 9/16 | 13/16 | 15/16 | 5/16 | 11/16 |

**Compliance checks** · passes / planned. Compliance requires both checks.

| Arm | Decision correct | Verifier passed |
| --- | --- | --- |
| biomni_staged_only | 61/96 | 37/96 |
| claude_code_no_surface | 87/96 | 53/96 |
| codex_no_surface | 85/96 | 48/96 |
| codex_with_surface | 91/96 | 61/96 |

<details><summary>Score manifests and run conditions</summary>

Shared settings: `fig3a-sc02note-v1|budget=1800s,5000000tok|seeds=20262101,20262102,20262201,20262202|prompt=instruction:sha256:aa9d4b88b9d72d4fcdc7ef410818f216b266e59df6cdd70b27cf6fc2ae9df428|feedback=none`

- [V3V4-20261107-v11-I-biomni-staged-only](https://nomomoko.github.io/ontoflow-fig3a-evidence/runs/fig3a-v3v4-20261107/scores/V3V4-20261107-v11-I-biomni-staged-only/manifest.json) · [run index](https://nomomoko.github.io/ontoflow-fig3a-evidence/runs/fig3a-v3v4-20261107/)
- [V3V4-20261107-v11-I-claude-code-no-surface](https://nomomoko.github.io/ontoflow-fig3a-evidence/runs/fig3a-v3v4-20261107/scores/V3V4-20261107-v11-I-claude-code-no-surface/manifest.json) · [run index](https://nomomoko.github.io/ontoflow-fig3a-evidence/runs/fig3a-v3v4-20261107/)
- [V3V4-20261107-v11-I-codex-no-surface](https://nomomoko.github.io/ontoflow-fig3a-evidence/runs/fig3a-v3v4-20261107/scores/V3V4-20261107-v11-I-codex-no-surface/manifest.json) · [run index](https://nomomoko.github.io/ontoflow-fig3a-evidence/runs/fig3a-v3v4-20261107/)
- [V3V4-20261107-v11-I-codex-with-surface](https://nomomoko.github.io/ontoflow-fig3a-evidence/runs/fig3a-v3v4-20261107/scores/V3V4-20261107-v11-I-codex-with-surface/manifest.json) · [run index](https://nomomoko.github.io/ontoflow-fig3a-evidence/runs/fig3a-v3v4-20261107/)

</details>

#### Compliant · deepseek/deepseek-chat · Development

Roster `fig3a-24case-sc02note-v1` · Passes / planned slots.

| Arm | Independent | Scored |
| --- | --- | --- |
| cellvoyager_v1 | 43/96 | 96 |

**Passes by reporting group**

| Arm | A | B | C | D | E | F |
| --- | --- | --- | --- | --- | --- | --- |
| cellvoyager_v1 | 3/16 | 8/16 | 11/16 | 7/16 | 4/16 | 10/16 |

**Compliance checks** · passes / planned. Compliance requires both checks.

| Arm | Decision correct | Verifier passed |
| --- | --- | --- |
| cellvoyager_v1 | 62/96 | 47/96 |

<details><summary>Score manifests and run conditions</summary>

Shared settings: `fig3a-sc02note-v1|budget=1800s,5000000tok|seeds=20262101,20262102,20262201,20262202|prompt=instruction:sha256:aa9d4b88b9d72d4fcdc7ef410818f216b266e59df6cdd70b27cf6fc2ae9df428|feedback=none`

- [V3V4-20261107-v11-I-cellvoyager-v1](https://nomomoko.github.io/ontoflow-fig3a-evidence/runs/fig3a-v3v4-20261107/scores/V3V4-20261107-v11-I-cellvoyager-v1/manifest.json) · [run index](https://nomomoko.github.io/ontoflow-fig3a-evidence/runs/fig3a-v3v4-20261107/)

</details>
