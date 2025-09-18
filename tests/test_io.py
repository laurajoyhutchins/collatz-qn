"""Tests for test_io.py.
Covers core functionality of q(n) analysis (I/O, counts, fitting, plotting).
"""

from qn.io import load_residue_support
def test_load_residue_support_columns():
    df = load_residue_support()
    for c in ["residue_mod_4096","minimal_k","support_size","support_primes"]:
        assert c in df.columns
