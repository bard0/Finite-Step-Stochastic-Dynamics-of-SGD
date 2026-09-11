# Claims and Evidence

## Confirmed / analytical

### C1. Low-order descriptor insufficiency for mean-square stability

An explicit scalar finite-sum SGD construction can match the population Hessian and zero-order gradient-noise covariance while changing the exact finite-step second-moment stability threshold through multiplicative noise geometry.

For the solvable model:

\[
q=(1-\eta\lambda)^2+\eta^2G_\Sigma,
\qquad
\eta_c=\frac{2\lambda}{\lambda^2+G_\Sigma}.
\]

**Status:** confirmed analytical existence result.

### C2. Additive-noise baseline

For `G_Sigma=0`, the mean-square boundary reduces to the deterministic scalar boundary `eta_c=2/lambda`.

**Status:** confirmed analytical baseline.

### C3. iid filtration correction

For conditionally unbiased, independently resampled with-replacement minibatches, centered innovations are martingale differences; a generic nonzero cross-time covariance `E[xi_s xi_t^T]` is therefore not the correct universal iid descriptor.

**Status:** confirmed methodological correction.

## Controlled numerical evidence

### E1. M9 threshold prediction

Frozen `G_Sigma` predictor substantially improves system-level and matched A-B stability-threshold prediction in the tested 1D family.

- system-level `eta_c`: R2 `0.7791`, Spearman `0.8714`;
- matched `Delta eta_c`: R2 `0.8485`, Spearman `0.9543`.

**Status:** controlled confirmatory evidence for the tested family; not yet a neural-network or general minibatch claim.

### E2. M9 sharpness prediction

The projected-noise baseline already explains most of the absolute sharpness gap (R2 `0.9519`), while the noise-geometry model improves to R2 `0.9943`.

For matched A-B differences, the noise-geometry model reaches R2 `0.9835` and Spearman `0.9777` while the matched zero-order baseline predicts zero.

**Status:** incremental support for noise geometry; explicitly not evidence that leading projected-noise theory fails for absolute sharpness.

## Internally proved but novelty-limited theory

### T1. Higher-order covariance jets

Fixed-horizon covariance expansions identify additional local stochastic information beyond additive covariance:

- order 4: `D^2 Sigma` and the third cumulant;
- order 5: `D Sigma`, `D^3 Sigma`, fourth-cumulant sectors, plus deterministic higher geometry.

**Status:** internally derived/audited; generic ingredients overlap strongly with stochastic modified equations, weak expansions, B-series, and cumulant theory. No broad novelty claim.

## Exploratory

### X1. Statistical non-regularity of stochastic stability boundaries

Near `rho(M)=1`, consistent operator estimation may not imply uniformly reliable binary stability decisions under local alternatives.

**Status:** active hypothesis; theorem not yet established.

### X2. Fourth-moment / random-Hessian separation beyond second-order closures

Matched second-order descriptors may fail to determine stationary fourth moments or higher harmonic stability when random Hessian distributions differ in higher moments.

**Status:** exploratory theory branch; not yet promoted to a project claim.

## Falsified / downgraded

- Universal Koopman/spectral theory of SGD as the main contribution.
- Generic claim that iid SGD has exploitable centered temporal noise covariance.
- Operator difference as sufficient evidence of spectral difference.
- Third-cumulant-only novelty.
- Pure second-order covariance closure as a complete neural SGD description.
