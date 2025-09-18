# TODO

> Priority legend — **[P0] now**, **[P1] next**, **[P2] later**. Durations are rough effort estimates.

---

## Quick Wins
- [ ] **[P0]** Remove duplication of findings file: keep `reports/summary_findings.md` and delete or symlink `results/summary_findings.md` (single source of truth).
- [ ] **[P0]** Fix `Makefile`:
  - add target `residuals` (calls `scripts/compute_and_plot_residuals.py`) and include it in `all`.  
  - drop redundant `data:` alias or make it depend on `counts`.  
  - add `help` target and phony guards; make `plots` depend on `counts`; make `fit` depend on `counts`.  
  - `verify` should conditionally skip when checksum file is absent (or fail with clear message).
- [ ] **[P0]** Centralize excluded primes as a constant, e.g. `EXCLUDED_PRIMES = {2, 3}` in `src/qn/counts.py`, and import everywhere (avoid magic numbers).
- [ ] **[P0]** Refactor scripts to reuse library functions (no duplicated counting logic):
  - `scripts/fit_zipf_models.py` and `scripts/compute_and_plot_residuals.py` should call `build_prime_counts(...)` instead of recomputing with `ast.literal_eval`.
- [ ] **[P0]** Pin dependencies with versions (either `pyproject.toml` or expand `requirements.txt`) and document Python 3.10–3.11 support in README.

---

## Documentation
- [ ] **[P0]** Expand `README.md` with an **exact, copy-paste** quickstart:
  - create venv, install deps, run `make all`, where outputs land, how to view figures.
- [ ] **[P1]** Add “Reproduction checklist” (data present, checksum verified, expected row/prime counts).
- [ ] **[P1]** Enrich `reports/summary_findings.md`:
  - brief methodology for log–log fitting, explicit exclusions (2,3), definition of K, and caveats on finite-size bias.
  - link each figure/table to its generating command.
- [ ] **[P2]** Start `docs/` (MkDocs + Material): API docs from docstrings, pipeline diagram, and model definitions (1/p, relaxed Zipf).
- [ ] **[P2]** Add dataset provenance and license notes for `data/raw/*` (source, scope, constraints).

---

## Analysis
- [ ] **[P0]** Provide **weighted** log–log regression or Poisson GLM; current OLS on logs is heteroskedastic. Report both and compare.
- [ ] **[P1]** Add MLE-based fit for discrete power-law / truncated zeta; compare AIC/BIC against 1/p and relaxed Zipf.
- [ ] **[P1]** Residual diagnostics: standardized/studentized residuals, QQ plots, influence (Cook’s D), and heteroskedasticity checks.
- [ ] **[P1]** Bootstrap CIs for \(\delta\), \(p_0\), and \(C\); report uncertainty bands on plots.
- [ ] **[P1]** Sensitivity analyses:
  - vary small-prime exclusions (beyond {2,3});  
  - exclude tail primes with very low counts;  
  - re-fit on halves of the prime set (cross-validation style).
- [ ] **[P2]** Implement explicit **1/p** baseline (no fitting) and show residuals relative to that law side-by-side with relaxed Zipf.

---

## Data
- [ ] **[P0]** Add `data/raw/*.sha256` and make `make verify` check them.
- [ ] **[P1]** Document contents of `qn_exponents_package.zip` (files, shapes, schema, units); include a tiny README inside the zip.
- [ ] **[P1]** Provide a **small fixture** CSV (≤50 rows, ≤15 primes) for fast tests and CI.
- [ ] **[P2]** Define a simple data schema (Pandera or pydantic) and validate columns on load.

---

## Code
- [ ] **[P0]** Refactor scripts into thin CLIs using `argparse` (input/output paths, label thinning, K selection); move logic into `src/qn`.
- [ ] **[P0]** Adopt consistent docstring style (NumPy/Google); add type hints throughout (`numpy.typing.NDArray`, return types).
- [ ] **[P1]** Add modules:
  - `src/qn/activation.py` (compute activation curves; exposes pure functions).  
  - `src/qn/sweep.py` (slope vs K generator with a single entry point).
- [ ] **[P1]** Add scripts:
  - `scripts/compute_activation.py` → writes `activation_curve.csv`, `activation_summary.csv`, and `figures/activation_curves_top.png`.  
  - `scripts/sweep_slopes.py` → writes `slope_vs_K.csv` (+ figure).
- [ ] **[P2]** Introduce `logging` (INFO/DEBUG) and replace prints; fail with clear exceptions on missing inputs.

---

## Testing
- [ ] **[P0]** Add unit tests to cover activation curve and slope-vs-K generation (deterministic small fixture).
- [ ] **[P1]** Plot tests: write PNGs from fixture and compare perceptual hash / size & axis metadata (avoid brittle pixel-perfect asserts).
- [ ] **[P1]** Regression tests on fit outputs:
  - slope \(\in [-0.8,-0.5]\) (loose) and RMSE range on fixture; best-fit row consistency.
- [ ] **[P1]** IO tests for `processed_path`/`raw_path` and schema validation.
- [ ] **[P2]** CLI tests for scripts (argparse help & basic run) via `pytest` and `pytest-console-scripts`.

---

## Reproducibility & Infrastructure
- [ ] **[P0]** Ensure `make all` fully regenerates **every** artifact now in repo (`figures/*`, `data/processed/*`), including residual plots.
- [ ] **[P1]** GitHub Actions CI: ruff (lint), black (format), mypy (types), pytest (unit + fixture run), and a smoke `make all` on fixture.
- [ ] **[P1]** Pre-commit hooks: `ruff`, `black`, `end-of-file-fixer`, `trailing-whitespace`.
- [ ] **[P1]** Package for install:
  - `pyproject.toml` with `project.scripts` entry points; rename module to `collatz_qn` to avoid overly generic `qn` (optional but cleaner).
- [ ] **[P2]** Version processed outputs under `data/processed/YYYYMMDD/` and update `.gitignore` to allow tiny CSV snapshots for the fixture.

---

## Future Directions
- [ ] **[P2]** Extend to larger \(K\) as data becomes available; track slope vs K with uncertainty bands.
- [ ] **[P2]** Compare with probabilistic prime-occurrence models; explore modular restrictions beyond 2 and 3.
- [ ] **[P2]** Publish a Zenodo snapshot and update `CITATION.cff` with DOI; add a short “How to cite” in README.

---