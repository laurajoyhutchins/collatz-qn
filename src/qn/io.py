"""I/O utilities for q(n) analysis.

Functions:
- load_residue_support(): Load residue prime support CSV, parse support_primes column.
- processed_path(name): Build path to processed CSV or JSON in data/processed/.
"""

import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

def raw_path(name: str) -> Path:
    return ROOT / "data" / "raw" / name

def processed_path(name: str) -> Path:
    p = ROOT / "data" / "processed" / name
    p.parent.mkdir(parents=True, exist_ok=True)
    return p

def load_residue_support() -> pd.DataFrame:
    return pd.read_csv(raw_path("full_residue_prime_support.csv"))
