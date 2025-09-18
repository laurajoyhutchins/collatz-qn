"""Fit distributional models to prime frequency data.

Inputs:
- data/processed/prime_counts.csv

Outputs:
- data/processed/fit_results_grid.csv
- data/processed/best_fit.json

Usage:
  python scripts/fit_zipf_models.py
Or via Makefile: make fit
"""

import json, numpy as np, pandas as pd
from qn.io import load_residue_support, processed_path
from qn.fitting import grid_fit
from qn.counts import build_prime_counts

if __name__ == "__main__":
    df = load_residue_support()
    # Get prime counts using centralized function
    prime_counts = build_prime_counts(df)
    primes = np.array(prime_counts["prime"].values, dtype=float)
    y = np.array(prime_counts["count"].values, dtype=float)

    p0_grid = np.linspace(0.0, 10.0, 21)
    grid = grid_fit(primes, y, p0_grid)
    grid.to_csv(processed_path("fit_results_grid.csv"), index=False)

    # best row by RMSE
    best = grid.iloc[grid["RMSE_log"].argmin()].to_dict()
    best["model"] = "C/(p+p0)^(1+delta)"
    with open(processed_path("best_fit.json"), "w") as fh:
        json.dump(best, fh, indent=2)
    print("Wrote data/processed/fit_results_grid.csv and best_fit.json")
