# G8.10 — Neural mixed-fourth transfer test

## Question

Does the mixed fourth directional derivative

\[
\chi_{mix}=D^4L[u,u,v,v]
\]

add held-out predictive information for future neural-SGD sharpness beyond a frozen lower-order stochastic/curvature/finite-step/eigenspace-rotation baseline?

Here `u` is the top Hessian eigenvector. The transverse direction `v` is derived from the component of the sharpness gradient orthogonal to `u` and is frozen when estimating the directional fourth derivative.

## Experimental sequence

- **A1:** repaired convergence-driven top-eigenvector estimation and verified mixed-fourth estimator feasibility.
- **B0:** checked descriptor replication across primary sustained-EoS regimes.
- **B1:** validated finite-horizon sharpness targets.
- **B2:** comparator-complete attempt; insufficient for the intended final incremental-value claim.
- **B3 / B3-R1:** repaired the exact nearest-point projection used for paper-faithful Liao applicability. Eligibility remained sparse.
- **B4:** fresh prospective held-out primary test plus a secondary Liao-mechanistic subset.

## B4 design

Primary settings:

- batch size: `200`;
- `eta`: `0.018`, `0.020`;
- fresh seed groups: `30..45`;
- primary horizon: `H=10`;
- target rollouts per checkpoint: `32`;
- usable primary checkpoints: `30`;
- independent seed groups: `16`.

The primary model ladder ended with:

- `N3`: strongest frozen baseline including lower-order stochastic, curvature, verified finite-step, and eigenspace-rotation information;
- `N4 = N3 + chi_mix`.

Evaluation used grouped held-out ridge regression with seed identity as the independent grouping unit. Uncertainty was evaluated by seed-group bootstrap; the descriptor null was tested by grouped permutation.

## Primary result

| metric | N3 | N4 / increment |
|---|---:|---:|
| MAE | 2.092574 | 1.994240 |
| RMSE | 2.669425 | 2.654023 |
| R2 | 0.717954 | 0.721200 |
| Spearman | 0.830033 | 0.855395 |
| MAE gain | — | 0.046992 |
| Delta R2 | — | 0.003245 |
| residual Spearman | — | 0.327697 |
| sign agreement | — | 0.633333 |
| paired permutation p | — | 0.042791 |

Seed-group bootstrap:

- MAE-gain 95% CI: `[-0.061881, 0.151094]`;
- `Delta R2` 95% CI: `[-0.056984, 0.041353]`;
- residual-Spearman 95% CI: `[-0.070420, 0.631139]`;
- sign-agreement 95% CI: `[0.4375, 0.80645]`.

The frozen primary decision required substantially stronger and regime-consistent evidence than a nominal permutation signal alone.

**Primary verdict:** `FAIL_NO_PRIMARY_NEURAL_INCREMENTAL_VALUE`.

## Eta-stratified result

| eta | n | MAE N3 | MAE N4 | MAE gain |
|---:|---:|---:|---:|---:|
| 0.018 | 14 | 1.894703 | 1.615007 | 0.147620 |
| 0.020 | 16 | 2.265710 | 2.326069 | -0.026640 |

The `eta=0.018` stratum shows a positive bootstrap interval for MAE gain, while the `eta=0.020` stratum does not. This heterogeneity is **exploratory** and does not revise the primary verdict.

## Secondary Liao-mechanistic subset

The secondary test used exact KKT projection and paper-faithful local applicability gates before constructing the moving reference prediction.

Most candidate states failed the local alpha/beta prerequisites after exact projection; one additional case had non-converged exact SQP. Only 3 independent seed groups survived the full moving-reference pipeline, below the frozen minimum for a formal mechanism verdict.

**Secondary verdict:** `INCONCLUSIVE_LIAO_MOVING_REFERENCE_ATTRITION`.

This is an applicability/sample-size limitation, not evidence that the Liao mechanism itself is false.

## Interpretation

B4 falsifies the strong tested claim that `chi_mix` provides a stable regime-robust held-out increment over the strongest frozen baseline in this neural setup.

It does **not** establish that `chi_mix` is universally useless. The observed eta heterogeneity is retained only as a hypothesis-generating signal and must survive influence, residualization, collinearity, negative-control, and independent prospective tests before any narrower claim can be promoted.
