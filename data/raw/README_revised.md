## DEPRECATED

This file has been superseded by the top-level README.md.

---

# Collatz q(n) Research Package

This package provides data and tools for studying the **Collatz numerator sequence** q(n).  
It is organized into a dataset, helper scripts, and supporting documentation.

---

## Files

- **`qn_exponents_rep_k12_filled.npz`**  
  Compressed dataset (sparse matrix) storing prime factorizations of q(n).

- **`qn_exponents_rep_k12_filled_README.txt`**  
  Technical description of the dataset format.

- **`helper_scripts.py`**  
  Python utilities for loading the dataset, retrieving factorizations, and computing q(n).

- **`collatz_q_notes.md`**  
  Detailed mathematical notes and derivations (see documentation).

---

## What is q(n)?

The sequence q(n) arises from the **Collatz map**.  
It is determined by the parity code of the trajectory of n under iteration of the Collatz function.  
Each q(n) is an integer capturing structural information about the orbit.

- Always odd.  
- Never divisible by 3.  
- Encodes trajectory information in its prime factorization.

---

## Dataset Overview

- **Rows**: odd n < 2048 (representatives of residue classes mod 2^12).  
- **Columns**: odd primes (prime 2 excluded since ν₂(q(n))=ν₂(n)).  
- **Entries**: exponents e where p^e ∥ q(n).  
- **Format**: SciPy CSR sparse matrix.  
- **Extras**:  
  - `row_ids`: actual n values.  
  - `col_primes`: prime labels.

---

## Quick Start

```python
from helper_scripts import load_dataset, factorization_row

M, primes, rows = load_dataset("qn_exponents_rep_k12_filled.npz")
factors = factorization_row(M, primes, rows, 0)
print(factors)  # prime factorization of q(n) for first representative
```

---

## Documentation

For the deeper mathematics behind q(n), including parity code, structural laws, and arithmetic properties, see:  
- [collatz_q_notes.md](./collatz_q_notes.md)
