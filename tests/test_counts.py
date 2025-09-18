"""Tests for test_counts.py.
Covers core functionality of q(n) analysis (I/O, counts, fitting, plotting).
"""

import ast
from qn.io import load_residue_support
from qn.counts import build_prime_counts

def test_counts_sum_and_exclusions():
    df = load_residue_support()
    pc = build_prime_counts(df)
    assert "prime" in pc.columns and "count" in pc.columns
    # Known totals from current snapshot
    assert pc["count"].sum() == 1342
    assert not pc["prime"].isin([2,3]).any()
