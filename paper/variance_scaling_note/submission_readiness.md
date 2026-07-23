# Submission readiness — REVIEW, not ready

This package is **not READY**. This table records bounded engineering checks; scientific content, submission declarations, and author metadata remain under PI authority.

| Gate | Status | Evidence / required action |
|---|---|---|
| manuscript source exists | FAIL | `paper/variance_scaling_note/manuscript.tex` is absent; no alternative was searched. |
| manuscript compiles | BLOCKED | No source at the specified path and no LaTeX engine on `PATH`. |
| figures exist | FAIL | Requested PDF figures are absent; accepted PNG inputs were absent and explicit user instructions prohibit adding PDFs/PNGs/binaries. |
| figures are referenced | BLOCKED | Manuscript source is absent. |
| bibliography verified | BLOCKED | No manuscript citation keys were available; `references.bib` intentionally contains no invented records. |
| placeholders absent | PASS | No compile-only placeholders were created. |
| internal references resolved | BLOCKED | Manuscript source is absent and compilation could not run. |
| supplement tests pass | PASS | Source and extracted-package runs each passed all 19 tests. |
| supplement demonstration passes | PASS | Source, portable-root, and extracted-ZIP demonstrations passed required residual thresholds. |
| ZIP content boundary passes | PASS | Temporary deterministic ZIP audit contained exactly the declared source tree and no prohibited entries. |
| no legacy/data leakage | PASS | Supplement inventory contains only declared source, tests, demo, README, and requirements; no data/notebooks/artifacts/figures/manuscript files. |
| author metadata complete | PI REVIEW | Manuscript source is absent; PI must provide/confirm metadata. |
| email complete | PI REVIEW | Manuscript source is absent; PI must provide/confirm email. |
| affiliation complete | PI REVIEW | Manuscript source is absent; PI must provide/confirm affiliation. |
| word limit reviewed | PI REVIEW | No venue limit or manuscript source was supplied; word counts unavailable. |
| AI declaration present | PI REVIEW | PI-managed manuscript/declaration not supplied. |
| funding declaration present | PI REVIEW | PI-managed manuscript/declaration not supplied. |
| competing-interest declaration present | PI REVIEW | PI-managed manuscript/declaration not supplied. |
| data/code availability statement present | PI REVIEW | PI-managed manuscript/declaration not supplied. |

## PI actions required

1. Supply `manuscript.tex` at the specified path, including PI-approved author, affiliation, email, declaration, and availability text.
2. Supply the three accepted PNG figure inputs or explicitly authorize another verified accepted source.
3. Resolve the explicit binary-file prohibition before retaining the required PDFs and `supplement.zip`.
4. Provide verified BibTeX records if the manuscript uses citations.
5. Review venue-specific word limits and all submission declarations.
