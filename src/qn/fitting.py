"""Model fitting utilities for prime factor distributions in q(n).

Functions:
- fit_loglog(primes, counts, p0): Fit log-log regression to counts ~ C/(p+p0)^{1+δ}.
- grid_fit(primes, counts, p0_grid): Sweep over p0 values, fit each, return DataFrame of fit metrics.
- predict_counts(primes, C, p0, delta): Predict expected counts under best-fit model.
- residuals_table(primes, observed, C, p0, delta): Build table of observed vs predicted counts, residuals, errors.
"""

import numpy as np
import pandas as pd

def fit_loglog(primes: np.ndarray, counts: np.ndarray, p0: float=0.0):
    """ Fit log(counts) = intercept + slope * log(p+p0). Returns dict with keys: intercept, slope, R2, RMSE_log. """
    x = np.log(primes + p0)
    y = np.log(counts)
    X = np.vstack([np.ones_like(x), x]).T
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    intercept, slope = beta
    yhat = X @ beta
    ss_res = np.sum((y - yhat)**2)
    ss_tot = np.sum((y - y.mean())**2)
    r2 = 1 - ss_res/ss_tot if ss_tot > 0 else np.nan
    rmse = float(np.sqrt(np.mean((y - yhat)**2)))
    return {"intercept": float(intercept), "slope": float(slope), "R2": float(r2), "RMSE_log": rmse}

def grid_fit(primes: np.ndarray, counts: np.ndarray, p0_grid):
    """ Evaluate fit_loglog across a grid of p0 values. Returns a DataFrame with columns ['p0','slope','delta','logC','C_eff','R2','RMSE_log']. """
    rows = []
    for p0 in p0_grid:
        m = fit_loglog(primes, counts, p0)
        delta = -1 - m["slope"]
        rows.append({
            "p0": float(p0),
            "slope": m["slope"],
            "delta": float(delta),
            "logC": m["intercept"],
            "C_eff": float(np.exp(m["intercept"])),
            "R2": m["R2"],
            "RMSE_log": m["RMSE_log"],
        })
    return pd.DataFrame(rows).sort_values("p0")


def predict_counts(primes: np.ndarray, C: float, p0: float, delta: float) -> np.ndarray:
    return C / np.power(primes + p0, 1.0 + delta)

def residuals_table(primes: np.ndarray, observed: np.ndarray, C: float, p0: float, delta: float) -> pd.DataFrame:
    pred = predict_counts(primes, C, p0, delta)
    df = pd.DataFrame({
        "prime": primes.astype(int),
        "observed_count": observed.astype(float),
        "predicted_count": pred.astype(float),
    }).sort_values("prime").reset_index(drop=True)
    df["residual"] = df["observed_count"] - df["predicted_count"]
    df["log_residual"] = np.log(df["observed_count"]) - np.log(df["predicted_count"])
    df["abs_pct_error"] = np.abs(df["residual"]) / np.maximum(df["observed_count"], 1.0)
    return df
