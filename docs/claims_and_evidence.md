# Claims and Evidence — v1 Freeze

**Freeze date:** 2026-09-30

## Confirmed analytical / methodological

### C1. Low-order descriptor insufficiency for finite-step mean-square stability

An explicit scalar finite-sum construction can match the lower-order reference geometry while changing the exact mean-square stability threshold through state-dependent stochastic geometry:

\[
q=(1-\eta\lambda)^2+\eta^2G_\Sigma,
\qquad
\eta_c=\frac{2\lambda}{\lambda^2+G_\Sigma}.
\]

**Status:** confirmed analytical existence result.

### C2. Additive-noise control

For \(G_\Sigma=0\), the boundary reduces to \(2/\lambda\). Controlled additive zero-mean noise does not support a generic physical mean spectral-shift mechanism by noise amplitude alone.

**Status:** confirmed analytical/control result.

### C3. iid temporal-covariance correction

Under conditionally unbiased independently resampled with-replacement minibatching, centered innovations are martingale differences; generic centered cross-time covariance is not a universal iid-SGD memory descriptor.

**Status:** confirmed methodological correction.

## Controlled numerical evidence

### E1. Controlled Duffing validation

Under deliberately controlled assumptions, the spectral perturbation predictor achieved approximately:

- MAE \(1.5\times10^{-7}\);
- median relative error \(2.5\times10^{-3}\);
- Spearman correlation \(0.999\).

**Status:** strong controlled validation of the machinery, not a universal SGD claim.

### E2. M9 stability prediction

Noise-geometry predictors achieve:

- system-level \(\eta_c\): \(R^2=0.7791\), Spearman \(0.8714\);
- matched \(\Delta\eta_c\): \(R^2=0.8485\), Spearman \(0.9543\).

**Status:** controlled confirmatory evidence for the tested family.

### E3. M9 sharpness prediction

- absolute sharpness gap: projected-noise baseline \(R^2=0.9519\), noise-geometry \(R^2=0.9943\);
- matched \(\Delta S\): noise-geometry \(R^2=0.9835\), Spearman \(0.9777\).

**Status:** incremental support for noise geometry, strongest in matched-system separation.

## Confirmatory negative / inconclusive

### N1. G8.10-B4 neural incremental-value test

Adding \(\chi_{mix}=D^4L[u,u,v,v]\) to the strongest frozen lower-order baseline did not jointly satisfy the preregistered magnitude, uncertainty, residual-correlation, sign, and cross-regime robustness gates.

**Status:** `FAIL_NO_PRIMARY_NEURAL_INCREMENTAL_VALUE`.

### N2. Secondary Liao moving-reference subset

Only 3 independent seed groups survived the exact applicability/moving-reference pipeline.

**Status:** inconclusive; no failure of the Liao mechanism is inferred.

## Exploratory / archived theory frontier

### X1. Eta-dependent \(\chi_{mix}\) heterogeneity

Observed MAE gain was \(+14.76\%\) at \(\eta=0.018\) and \(-2.66\%\) at \(\eta=0.020\).

**Status:** exploratory only.

### X2. Late matched-information finite-step theory

Local finite-horizon constructions show that separate pointwise/marginal descriptors can fail to determine future sharpness. Subsequent adversarial checks also show that compact frozen-law quotients need additional time-ordered information under genuinely moving stochastic laws.

**Status:** internally useful v2 theory frontier; no general v1 priority or long-horizon theorem claim.

## Falsified / downgraded

- generic additive-noise spectral mechanism;
- universal Koopman/spectral theory as the main contribution;
- universal centered temporal-covariance memory for ordinary iid SGD;
- simple linear \(K_{st}\) propagation as a universal neural closure;
- operator difference as sufficient evidence of spectral difference;
- third-cumulant-only or “higher moments matter” novelty;
- regime-robust neural incremental value of \(\chi_{mix}\) in G8.10-B4;
- any claim that the latest frozen local coupling quotient is already a full moving-PGD/general-SGD closure.

## v1 conclusion

The defensible project-level conclusion is a **descriptor-sufficiency map**: finite-step SGD can depend on state-dependent stochastic structure beyond scalar noise amplitude, but progressively richer descriptors must be justified by observable or held-out predictive consequences rather than by formal expandability alone.
