# Collatz q(n) Research

This repository contains data, code, and reports for studying the **Collatz numerator sequence** q(n).  
The project explores prime factor frequencies, distributional fits, and structural trends in q(n) across residue classes.

---

## What is q(n)?

The sequence q(n) arises from the **Collatz map**.  
It is determined by the parity code of the trajectory of n under iteration of the Collatz function.  
Each q(n) is an integer encoding orbit structure in its prime factorization.

Properties:

- Always odd.  
- Never divisible by 3.  
- Encodes trajectory information in its factorization pattern.

---

## Repository Layout

```
collatz-qn/
├── data/
│   ├── raw/         # Source datasets (e.g. qn_exponents_package.zip, full_residue_prime_support.csv)
│   └── processed/   # Derived tables (prime counts, fits, activation curves, slope sweeps)
├── figures/         # Generated plots (histograms, residuals, activation curves, slope vs K)
├── reports/         # Written findings and notes
├── scripts/         # Analysis scripts runnable via CLI or Makefile
├── src/qn/          # Library code (I/O, counts, fitting, plotting)
├── tests/           # Minimal tests
├── Makefile         # Common workflows (unpack, counts, fit, plots)
└── README.md        # This document
```

---

## Data Overview

- **Raw inputs**:  
  - `full_residue_prime_support.csv` – residue classes with prime support sets.  
  - `qn_exponents_package.zip` – compressed data package.  
  - `README_revised.md` – legacy description (deprecated).

- **Processed outputs** (examples):  
  - `prime_counts.csv` – frequency of each prime across residue classes.  
  - `fit_results_grid.csv`, `best_fit.json` – model fitting results.  
  - `activation_curve.csv`, `activation_summary.csv` – cumulative activation of primes over k.  
  - `slope_vs_K.csv` – fitted slopes across K values.  
  - `residuals_bestfit.csv` – deviations from best-fit model.

- **Figures**:  
  - Prime histograms (linear/log-y).  
  - Residual plots (per prime, observed vs predicted).  
  - Activation curves.  
  - Slope vs K trajectory.

---

## Usage

Requirements: Python 3.10+.
Dependencies and build requirements are managed via [`pyproject.toml`](./pyproject.toml).
Install core dependencies with:

```bash
python -m pip install .
```

Or for development (testing, linting, etc.):

```bash
python -m pip install .[dev]
```

You may also use `requirements.txt` for legacy installs.


## Build pipeline

```bash
# Unpack raw data
make unpack

# Generate prime counts and processed tables
make counts

# Fit models to distributions
make fit

# Produce figures
make plots
```

Or run scripts directly, e.g.:

```bash
python scripts/compute_counts.py
python scripts/fit_zipf_models.py
python scripts/plot_figures.py
python scripts/compute_and_plot_residuals.py
```

---

## Results

A summary of findings is in `reports/summary_findings.md`.  
Key result: At K=11, the distribution of prime factors in q(n) fits a Zipf-like law with slope ≈ -0.66, flatter than the ideal -1/p, consistent with finite-size effects.

---

## Contributing

Pull requests and issues welcome. Extend tests in `tests/` and keep processed outputs reproducible.

---

## License

MIT License. See `LICENSE`.

---

## Citation

If you use this work, please cite:

```
Author: Laura (research lead)
Project: Collatz q(n) Research
Repository: https://github.com/<to-be-determined>
Year: 2025
```
