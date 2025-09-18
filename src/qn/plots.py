"""Plotting utilities for q(n) analysis.

Functions:
- plot_histogram(df, logy, label_every): Plot histogram of prime frequencies.
- plot_residuals_vs_prime(residuals_df, label_every): Plot log-residuals per prime.
- plot_observed_vs_predicted(residuals_df): Scatter plot of observed vs predicted counts.
"""

import matplotlib.pyplot as plt
import pandas as pd

def plot_histogram(prime_counts: pd.DataFrame, logy: bool=False, label_every:int=0):
    """ Bar plot of prime counts. If logy=True set y-axis to log scale. If label_every>1 only label every Nth tick to reduce clutter. """
    x = prime_counts["prime"].astype(str).tolist()
    y = prime_counts["count"].tolist()
    plt.figure(figsize=(14,6))
    plt.bar(x, y)
    if logy:
        plt.yscale("log")
    if label_every and label_every > 1:
        labels = [xi if i % label_every == 0 else "" for i, xi in enumerate(x)]
        plt.xticks(range(len(x)), labels, rotation=90, ha="center")
    else:
        plt.xticks(range(len(x)), x, rotation=90, ha="center")
    plt.xlabel("Prime factor")
    plt.ylabel("Frequency across residue classes" + (" (log scale)" if logy else ""))
    plt.title("Histogram of prime factors in q(n) residue classes")
    plt.tight_layout()
    return plt.gcf()


def plot_residuals_vs_prime(residuals_df: pd.DataFrame, label_every:int=0):
    """ Bar plot of per-prime log residuals (log observed − log predicted). Use label_every to thin x-axis labels. """
    x = residuals_df["prime"].astype(str).tolist()
    y = residuals_df["log_residual"].tolist()
    plt.figure(figsize=(14,6))
    plt.bar(range(len(x)), y)
    if label_every and label_every > 1:
        labels = [xi if i % label_every == 0 else "" for i, xi in enumerate(x)]
    else:
        labels = x
    plt.xticks(range(len(x)), labels, rotation=90, ha="center")
    plt.axhline(0.0)
    plt.xlabel("Prime")
    plt.ylabel("Log residual (observed − predicted)")
    plt.title("Residuals per prime (log scale difference)")
    plt.tight_layout()
    return plt.gcf()

def plot_observed_vs_predicted(residuals_df: pd.DataFrame):
    """ Scatter plot of predicted vs observed counts per prime with y=x reference line. """
    plt.figure(figsize=(6,6))
    obs = residuals_df["observed_count"].values
    pred = residuals_df["predicted_count"].values
    plt.scatter(pred, obs, s=10)
    lim = max(obs.max(), pred.max())
    plt.plot([0, lim], [0, lim])
    plt.xlabel("Predicted count")
    plt.ylabel("Observed count")
    plt.title("Observed vs predicted counts per prime")
    plt.tight_layout()
    return plt.gcf()
