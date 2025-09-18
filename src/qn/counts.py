"""Prime counting utilities.

Functions:
- build_prime_counts(df): Compute frequency of each prime from a DataFrame with column 'support_primes' (list of ints).
Returns DataFrame with columns ['prime','count'].
"""

import pandas as pd, ast
from collections import Counter
from .io import load_residue_support

def build_prime_counts(df: pd.DataFrame) -> pd.DataFrame:
    df2 = df.copy()
    df2["support_primes"] = df2["support_primes"].apply(ast.literal_eval)
    c = Counter()
    for primes in df2["support_primes"]:
        c.update([p for p in primes if p not in (2,3)])
    rows = []
    for p, cnt in c.items():
        rows.append({"prime": int(p), "count": int(cnt)})
    out = pd.DataFrame(rows).sort_values("prime").reset_index(drop=True)
    total = out["count"].sum()
    out["proportion"] = out["count"] / total if total > 0 else 0.0
    return out
