# Summary of Findings on Prime Factor Frequencies in q(n)

This document summarizes the current analysis results, linking to processed outputs and figures.

---

## 1. Data Basis

- Input: 1024 residue classes at K=11.  
- Total observed prime incidences: 1342 across 148 distinct primes.  
- By construction, 2 and 3 never appear.  
- Source: [`data/raw/full_residue_prime_support.csv`](../data/raw/full_residue_prime_support.csv)

---

## 2. Prime Counts

- [`data/processed/prime_counts.csv`](../data/processed/prime_counts.csv)  
- Histogram plots:  
  - Linear scale: [`figures/histogram_primes.png`](../figures/histogram_primes.png)  
  - Log scale: [`figures/histogram_primes_logy.png`](../figures/histogram_primes_logy.png)

---

## 3. Distribution Fits

- Pure 1/p hypothesis: underpredicts mid/large primes.  
- Relaxed Zipf form: best slope ≈ -0.66 (δ≈-0.34).  
- Processed outputs:  
  - [`data/processed/fit_results_grid.csv`](../data/processed/fit_results_grid.csv)  
  - [`data/processed/best_fit.json`](../data/processed/best_fit.json)  
- Residuals:  
  - [`data/processed/residuals_bestfit.csv`](../data/processed/residuals_bestfit.csv)  
  - Plots:  
    - [`figures/residuals_vs_prime.png`](../figures/residuals_vs_prime.png)  
    - [`figures/observed_vs_predicted.png`](../figures/observed_vs_predicted.png)

---

## 4. Activation Curves

- Cumulative counts of each prime across k.  
- Data:  
  - [`data/processed/activation_curve.csv`](../data/processed/activation_curve.csv)  
  - [`data/processed/activation_summary.csv`](../data/processed/activation_summary.csv)  
- Figure:  
  - [`figures/activation_curves_top.png`](../figures/activation_curves_top.png)

---

## 5. Slope vs K

- Fitted slopes converge toward -1 as K grows.  
- Data: [`data/processed/slope_vs_K.csv`](../data/processed/slope_vs_K.csv)  
- Figures:  
  - [`figures/slope_vs_K.png`](../figures/slope_vs_K.png)  
  - [`figures/prime_support_vs_K.png`](../figures/prime_support_vs_K.png)

---

## 6. Interpretation

- Flattened slope at K=11 reflects incomplete prime support.  
- Larger primes have not yet activated.  
- Structural restrictions (odd, non-multiples of 3) persist as corrections.  
- Expect steepening toward -1 with increasing K.

---

## Conclusion

The distribution of prime factors in q(n) at K=11 is best modeled by a Zipf-like law with slope ≈ -0.66.  
Evidence suggests finite-size effects explain the flattening. With larger K, convergence toward 1/p decay is expected, modulo structural restrictions.
