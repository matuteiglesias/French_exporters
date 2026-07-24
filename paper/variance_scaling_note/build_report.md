# Build report — REVIEW

## Task specification

```yaml
target_artifact: paper/variance_scaling_note/
permitted_paths:
  - paper/variance_scaling_note/
  - src/aggregation_lab/
  - tests/test_variance_identity.py
  - tests/test_scaling_decomposition.py
  - research/demos/variance_scaling_identity_demo.py
  - research/artifacts/variance_scaling_demo_v0_1/
  - requirements-dev.txt
frozen_scientific_meaning: PI-managed technical note; deterministic algebraic demonstration only.
inputs: Accepted implementation, tests, demonstration, and demonstration artifact directory.
expected_outputs: Clean portable supplement, deterministic ZIP, reports, and (blocked by explicit user binary prohibition) no PDF artifacts.
validation_command: PYTHONPATH=src python -m pytest -q tests/test_variance_identity.py tests/test_scaling_decomposition.py
forbidden_changes: No scientific changes, no data/notebooks/legacy inspection, no PDF/PNG/binary additions, no unrelated working-tree changes.
stop_condition: Supplement ZIP and reports validated; manuscript/figures documented as blocked where source/artifacts or explicit binary prohibition prevent production.
```

## Environment

- Timestamp (UTC): 2026-07-23.
- Python: `/tmp/variance-scaling-venv/bin/python`, Python 3.12.3.
- Operating system: Linux 6.12.13-x86_64 with glibc 2.39.
- Direct dependencies: `numpy==2.5.1`, `pandas==3.0.5`, `matplotlib==3.11.1`, `pytest==9.1.1`.
- LaTeX engine: unavailable. `latexmk`, `pdflatex`, `bibtex`, and `tectonic` were not found on `PATH`; no TeX distribution was installed.

## Sources used

- `src/aggregation_lab/{__init__.py,variance.py,scaling.py,checks.py}`.
- `tests/test_variance_identity.py` and `tests/test_scaling_decomposition.py`.
- `research/demos/variance_scaling_identity_demo.py`.
- `research/artifacts/variance_scaling_demo_v0_1/` was inspected only for the requested accepted-artifact filenames. The requested PNG inputs were absent.
- `requirements-dev.txt`.

## Files created

- `references.bib` (no records were invented because `manuscript.tex` was absent and therefore no citation keys were available).
- Clean portable `supplement/` source tree with the declared nine files.
- `supplement/requirements.txt` with exact direct versions recovered from the Python 3.12 validation environment.
- `supplement/README.md`.
- This report and `submission_readiness.md`.

No PDFs, PNGs, or ZIP file were retained in the repository, per the explicit user override prohibiting additions of PDF files, PNG files, and binaries.

## Figures and manuscript

- `manuscript.tex`: absent at the specified path. Per instruction, no alternative manuscript was searched for; compilation and manuscript static checks are blocked.
- Figure 1 PNG: absent from the accepted artifact directory.
- Figure 2 source PNGs: absent from the accepted artifact directory.
- Figure PDF creation is additionally blocked by the explicit prohibition on adding PDF files.
- Figure conversion/composition method: not run; there were no accepted PNG inputs and no PDF output may be retained.
- Mechanical edits to `manuscript.tex`: none.
- Manuscript word count: unavailable (specified manuscript source absent).
- Abstract word count: unavailable (specified manuscript source absent).

## Byte-identity verification

All copied accepted source files were compared with `cmp` and were byte-for-byte identical:

- four `aggregation_lab` modules;
- two test modules;
- the demonstration script.

The supplement tree contains regular files only; no symlinks were found.

## Validation

### Accepted source tests

```bash
PYTHONPATH=src /tmp/variance-scaling-venv/bin/python -m pytest -q \
  tests/test_variance_identity.py tests/test_scaling_decomposition.py
```

Result: `19 passed in 0.94s`.

### Accepted demonstration

```bash
cd /tmp/variance-scaling-source-demo.4ZphOj
PYTHONPATH=/workspace/French_exporters/src /tmp/variance-scaling-venv/bin/python \
  /workspace/French_exporters/research/demos/variance_scaling_identity_demo.py
```

Result: all checks passed. Measured maxima were designed covariance `2.776e-16`, scaling identity `5.551e-16`, and variance identity `1.665e-16`, all within the required thresholds. The run was performed in a temporary directory so its generated PNGs/CSVs did not change the repository.

### Portable supplement validation

The supplement was copied to `/tmp/variance-scaling-portable.p6IEAN`, then run from that independent root:

```bash
PYTHONPATH=src /tmp/variance-scaling-venv/bin/python -m pytest -q \
  tests/test_variance_identity.py tests/test_scaling_decomposition.py
PYTHONPATH=src /tmp/variance-scaling-venv/bin/python \
  research/demos/variance_scaling_identity_demo.py
```

Result: `19 passed in 0.94s`; all demonstration checks passed with the same measured maxima above. This confirms the copied demonstration uses only its extracted-root relative output path and does not require the parent repository, Git, data, notebooks, external environment variables, or absolute paths.

## Temporary ZIP audit

A deterministic ZIP was created **only under `/tmp`** for validation, using lexicographic order, fixed DOS timestamp `1980-01-01 00:00:00`, and normalized file permissions. Its SHA-256 was `b3dfea6e4804054daa8b2f6f397d6a1096d2a9509826105e5e84c48b7d819864`; size was `12357` bytes. Timestamp normalization was therefore available.

The ZIP contained exactly:

```text
README.md
requirements.txt
research/demos/variance_scaling_identity_demo.py
src/aggregation_lab/__init__.py
src/aggregation_lab/checks.py
src/aggregation_lab/scaling.py
src/aggregation_lab/variance.py
tests/test_scaling_decomposition.py
tests/test_variance_identity.py
```

The explicit boundary audit passed: no prohibited path, binary output, cache, parent traversal, absolute path, or undeclared file was present. The ZIP was extracted to `/tmp/variance-scaling-extract.70vhPY`; tests (`19 passed in 0.96s`) and demonstration checks passed again. It was not copied to `paper/variance_scaling_note/supplement.zip` because the explicit user override prohibits adding binaries.

## Warnings and blockers

1. The specified PI-managed manuscript source does not exist.
2. The three specified accepted PNG figure inputs do not exist in the accepted artifact directory.
3. The explicit user override prohibits committing or staging PDFs, PNGs, and any binary files. Consequently `manuscript.pdf`, `figures/figure_1.pdf`, `figures/figure_2.pdf`, and `supplement.zip` are intentionally absent.
4. No LaTeX toolchain is available, independently blocking compilation.
5. The fixed-seed reference residual values requested for README reporting are retained there; this validated Python 3.12 environment produced smaller, non-identical normal floating-point residuals listed above.
