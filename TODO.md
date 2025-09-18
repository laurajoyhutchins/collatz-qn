# TODO

## Documentation
- [ ] Expand `README.md` with worked examples (inline code snippets).
- [ ] Add more detail to `reports/summary_findings.md` (methodology, not just results).
- [ ] Consider setting up `docs/` with Sphinx or MkDocs.

## Analysis
- [ ] Extend residual analysis to include standardized residuals and QQ plots.
- [ ] Fit alternative models (e.g. log–logistic, truncated zeta).
- [ ] Explore sensitivity of slope to different exclusion rules (e.g. primes beyond threshold).
- [ ] Automate generation of LaTeX tables for fit parameters.

## Data
- [ ] Document `qn_exponents_package.zip` contents in detail.
- [ ] Add checksum files for raw data (`*.sha256`).
- [ ] Provide smaller test datasets for unit testing.

## Code
- [ ] Improve CLI argument parsing in `scripts/` (argparse instead of fixed paths).
- [ ] Add unit tests for plotting functions (image hash or metadata).
- [ ] Increase test coverage for activation curve and slope-vs-K code.
- [ ] Refactor duplicated code for counting primes across scripts.

## Infrastructure
- [ ] Continuous integration: set up GitHub Actions (lint, test).
- [ ] Add pre-commit hooks for formatting (black, isort).
- [ ] Publish package metadata (setup.cfg / pyproject.toml).
- [ ] Version outputs in `data/processed/` with timestamped subfolders.

## Future Directions
- [ ] Extend to larger K beyond 11 if data becomes available.
- [ ] Compare observed distributions with probabilistic models of prime occurrence.
- [ ] Investigate modular restrictions beyond 2 and 3 in more detail.
