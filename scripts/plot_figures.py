"""Generate histogram plots from prime counts.

Inputs:
- data/processed/prime_counts.csv

Outputs:
- figures/histogram_primes.png
- figures/histogram_primes_logy.png

Usage:
  python scripts/plot_figures.py
Or via Makefile: make plots
"""

import pandas as pd
from qn.io import processed_path
from qn.plots import plot_histogram

if __name__ == "__main__":
    pc = pd.read_csv(processed_path("prime_counts.csv"))
    # regular histogram
    fig1 = plot_histogram(pc, logy=False, label_every=max(1, len(pc)//30))
    fig1.savefig("figures/histogram_primes.png", dpi=150)
    # log y histogram
    fig2 = plot_histogram(pc, logy=True, label_every=max(1, len(pc)//30))
    fig2.savefig("figures/histogram_primes_logy.png", dpi=150)
    print("Wrote figures/*.png")
