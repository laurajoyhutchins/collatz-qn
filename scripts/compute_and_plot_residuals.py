"""Compute residuals under best-fit model and plot diagnostics.

Inputs:
- data/raw/full_residue_prime_support.csv
- data/processed/best_fit.json

Outputs:
- data/processed/residuals_bestfit.csv
- figures/residuals_vs_prime.png
- figures/observed_vs_predicted.png

Usage:
  python scripts/compute_and_plot_residuals.py
"""

import json, ast, numpy as np, pandas as pd
from qn.io import load_residue_support, processed_path
from qn.fitting import grid_fit, residuals_table, predict_counts
from qn.plots import plot_residuals_vs_prime, plot_observed_vs_predicted

if __name__ == "__main__":
    df = load_residue_support()
    df["support_primes"] = df["support_primes"].apply(ast.literal_eval)
    counts = {}
    for primes in df["support_primes"]:
        for p in primes:
            if p in (2,3): continue
            counts[p] = counts.get(p, 0) + 1
    primes = np.array(sorted(counts.keys()), dtype=float)
    y = np.array([counts[int(p)] for p in primes], dtype=float)

    # Load best fit
    with open(processed_path("best_fit.json"), "r") as fh:
        best = json.load(fh)
    p0 = float(best["p0"])
    delta = float(best["delta"])
    C = float(best["C_eff"])  # use intercept-derived C

    # Residuals table
    res_df = residuals_table(primes, y, C=C, p0=p0, delta=delta)
    out_csv = processed_path("residuals_bestfit.csv")
    res_df.to_csv(out_csv, index=False)

    # Plots
    label_every = max(1, len(res_df)//30)
    fig1 = plot_residuals_vs_prime(res_df, label_every=label_every)
    fig1.savefig("figures/residuals_vs_prime.png", dpi=150)

    fig2 = plot_observed_vs_predicted(res_df)
    fig2.savefig("figures/observed_vs_predicted.png", dpi=150)

    print("Wrote", out_csv, "and residual plots in figures/.")
