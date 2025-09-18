"""Compute prime frequency counts from raw residue support data.

Inputs:
- data/raw/full_residue_prime_support.csv

Outputs:
- data/processed/prime_counts.csv

Usage:
  python scripts/compute_counts.py
Or via Makefile: make counts
"""

import pandas as pd
from qn.io import load_residue_support, processed_path
from qn.counts import build_prime_counts

if __name__ == "__main__":
    df = load_residue_support()
    pc = build_prime_counts(df)
    pc.to_csv(processed_path("prime_counts.csv"), index=False)
    print("Wrote data/processed/prime_counts.csv")
