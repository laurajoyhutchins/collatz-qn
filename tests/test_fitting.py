"""Tests for test_fitting.py.
Covers core functionality of q(n) analysis (I/O, counts, fitting, plotting).
"""

import ast, numpy as np
from qn.io import load_residue_support
from qn.fitting import grid_fit

def test_relaxed_slope_range():
    df = load_residue_support()
    df["support_primes"] = df["support_primes"].apply(ast.literal_eval)
    counts = {}
    for primes in df["support_primes"]:
        for p in primes:
            if p in (2,3): continue
            counts[p] = counts.get(p, 0) + 1
    primes = np.array(sorted(counts.keys()), dtype=float)
    y = np.array([counts[int(p)] for p in primes], dtype=float)
    grid = grid_fit(primes, y, p0_grid=[0.0])
    slope = float(grid.iloc[0]["slope"])
    assert -0.8 <= slope <= -0.5
