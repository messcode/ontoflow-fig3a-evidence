# Frozen Fig. 3A full-blind development measurement

RV-01 and VA-01, two evidence views, four arms, two planned replicates. Each arm has eight planned slots. Development release. The frozen verifier flagged an out-of-range local catalog request. The subsequent replay matched the underlying request to its typed local rejection; the original verdict is retained. The final eight previously undispatched slots continued after a host dispatch interruption. Full-strict counts below use all planned slots; the board group mean uses scored observations.

| Arm | Phase | Planned | Attempts | Returned | Schema valid | Full strict | Model calls | Input incl. cache | Cached input | Output |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| biomni | [independent](scores/FB-6b93b6cc7356-biomni-I/manifest.json) | 8 | 8 | 8 | 8 | 0 | 40 | 38297 | 11648 | 14267 |
| biomni | [repair](scores/FB-6b93b6cc7356-biomni-R/manifest.json) | 8 | 8 | 8 | 8 | 0 | 8 | 20805 | 16384 | 14814 |
| claude | [independent](scores/FB-6b93b6cc7356-claude-I/manifest.json) | 8 | 8 | 8 | 8 | 1 | 40 | 264498 | 144000 | 17838 |
| claude | [repair](scores/FB-6b93b6cc7356-claude-R/manifest.json) | 8 | 8 | 8 | 8 | 3 | 8 | 68655 | 0 | 6805 |
| codex-query | [independent](scores/FB-6b93b6cc7356-codex-query-I/manifest.json) | 8 | 8 | 8 | 8 | 3 | 40 | 439646 | 346880 | 29111 |
| codex-query | [repair](scores/FB-6b93b6cc7356-codex-query-R/manifest.json) | 8 | 8 | 8 | 8 | 5 | 8 | 92536 | 88960 | 21446 |
| codex-static | [independent](scores/FB-6b93b6cc7356-codex-static-I/manifest.json) | 8 | 8 | 8 | 8 | 1 | 40 | 461203 | 359168 | 48246 |
| codex-static | [repair](scores/FB-6b93b6cc7356-codex-static-R/manifest.json) | 8 | 8 | 8 | 8 | 4 | 8 | 103338 | 99840 | 8346 |

[Roster](roster.json) · [Phase summaries](summary.json) · [Measurement and adjudication PR](https://github.com/messcode/Ontoflow/pull/127)
