# Claims and Evidence

## Confirmed / analytical

### C1. Low-order descriptor insufficiency for mean-square stability

An explicit scalar finite-sum SGD construction can match the population Hessian and zero-order gradient-noise covariance while changing the exact finite-step second-moment stability threshold through multiplicative noise geometry.

\[
q=(1-\eta\lambda)^2+\eta^2G_\Sigma,
\qquad
\eta_c=\frac{2\lambda}{\lambda^2+G_\Sigma}.
\]

**Status:** confirmed analytical existence result.

### C2. Additive-noise baseline

For `G_Sigma=0`, the mean-square boundary reduces to `eta_c=2/lambda`.

**Status:** confirmed analytical baseline.

### C3. iid filtration correction

For conditionally unbiased independently resampled with-replacement minibatches, centered innovations are martingale differences; generic nonzero cross-time centered covariance is not the missing universal iid descriptor.

**Status:** confirmed methodological correction.

## Controlled numerical evidence

### E1. M9 threshold prediction

Frozen `G_Sigma` predictors substantially improve system-level and matched A-B stability-threshold prediction in the tested 1D family.

- system-level `eta_c`: R2 `0.7791`, Spearman `0.8714`;
- matched `Delta eta_c`: R2 `0.8485`, Spearman `0.9543`.

**Status:** controlled confirmatory evidence for the tested family; not a general neural-SGD claim.

### E2. M9 sharpness prediction

The projected-noise baseline already explains most of the absolute sharpness gap (R2 `0.9519`), while the noise-geometry model improves to R2 `0.9943`. For matched A-B differences, the noise-geometry model reaches R2 `0.9835`, Spearman `0.9777`.

**Status:** incremental support for noise geometry; not evidence that leading projected-noise theory fails for absolute sharpness.

### E3. G8.10 estimator feasibility

The mixed-fourth descriptor `chi_mix = D^4L[u,u,v,v]` was made numerically measurable on the tested smooth neural model after convergence-driven Hessian eigensolver repair. Descriptor replication and finite-horizon target acquisition also passed their engineering/measurement gates before the final predictive test.

**Status:** measurement feasibility only. This does not imply predictive or causal relevance.

## Confirmatory negative / inconclusive evidence

### N1. G8.10-B4 primary neural incremental-value test

Frozen comparison: strongest baseline `N3` versus `N4=N3+chi_mix`, with grouped held-out evaluation on fresh seed groups.

Observed pooled metrics:

- MAE `2.0926 -> 1.9942`;
- MAE gain `0.04699`, 95% bootstrap CI `[-0.06188, 0.15109]`;
- `Delta R2 = 0.00325`, CI `[-0.05698, 0.04135]`;
- residual Spearman `0.3277`, CI crossing zero;
- sign agreement `0.6333`;
- paired permutation `p = 0.0428`.

The preregistered magnitude, uncertainty, residual-correlation, sign, and two-regime robustness gates were not jointly satisfied.

**Status:** `FAIL_NO_PRIMARY_NEURAL_INCREMENTAL_VALUE`. The strong regime-robust neural incremental-value claim is falsified for the tested B4 design.

### N2. G8.10-B4 secondary Liao-mechanistic subset

Only 3 independent seed groups survived the exact applicability/moving-reference pipeline; the frozen requirement was at least 6 total and at least 3 per primary eta.

**Status:** `INCONCLUSIVE_LIAO_MOVING_REFERENCE_ATTRITION`. No scientific failure of the Liao mechanism is inferred.

## Exploratory

### X1. Eta-dependent `chi_mix` effect

In the B4 eta-stratified analysis, MAE gain was `+14.76%` at `eta=0.018` and `-2.66%` at `eta=0.020`. Within-eta analyses also showed improvements, but these observations are post-hoc relative to the failed pooled confirmatory claim.

**Status:** exploratory only; requires influence, residualization, collinearity, and independent prospective confirmation before promotion.

### X2. Fourth-moment / random-Hessian separation beyond second-order closures

Matched second-order descriptors may fail to determine stationary fourth moments or higher harmonic stability when random Hessian distributions differ in higher moments.

**Status:** exploratory theory branch; not yet promoted to a project claim.

## Internally proved but novelty-limited theory

### T1. Higher-order covariance jets

Fixed-horizon covariance expansions identify local stochastic information beyond additive covariance, including covariance-field derivatives and higher cumulants.

**Status:** internally derived/audited; generic ingredients overlap strongly with stochastic modified equations, weak expansions, B-series, and cumulant theory. No broad novelty claim.

## Falsified / downgraded

- universal Koopman/spectral theory of SGD as the main contribution;
- generic claim that iid SGD has exploitable centered temporal noise covariance;
- operator difference as sufficient evidence of spectral difference;
- third-cumulant-only novelty;
- pure second-order covariance closure as a complete neural SGD description;
- regime-robust incremental predictive value of `chi_mix` under the preregistered G8.10-B4 design.
