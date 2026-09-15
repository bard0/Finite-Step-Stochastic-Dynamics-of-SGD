# Current Research State

Last synchronized with the project archive: **2026-09-15**.

## 1. Current question

Which stochastic information is required to predict finite-step SGD behavior near stability boundaries, and which candidate descriptors survive held-out neural transfer tests?

The earlier universal temporal-covariance hypothesis remains rejected for ordinary iid/with-replacement minibatching under standard conditional-unbiasedness assumptions. The main line therefore focuses on state-dependent stochastic geometry, finite-step dynamics, and falsifiable higher-order descriptors.

## 2. Confirmed mathematical core

### Scalar descriptor-insufficiency counterexample

There is an explicit finite-sum construction in which two systems share the same population objective locally, the same population Hessian `H`, and the same zero-order gradient-noise covariance `Sigma(0)`, but differ in state-dependent noise geometry and in the exact finite-step mean-square stability boundary.

For the solvable scalar model,

\[
q=(1-\eta\lambda)^2+\eta^2 G_\Sigma,
\qquad
\eta_c=\frac{2\lambda}{\lambda^2+G_\Sigma}.
\]

The additive control has `G_Sigma=0` and recovers `2/lambda`.

This is an existence / insufficiency statement, not a claim that multiplicative noise or mean-square stability theory is new.

## 3. M9 controlled evidence

M9 tests frozen predictors in a controlled 1D stochastic family.

- system-level `eta_c`: noise-geometry model R2 `0.7791`, Spearman `0.8714`;
- matched `Delta eta_c`: R2 `0.8485`, Spearman `0.9543`;
- absolute sharpness gap: projected-noise baseline R2 `0.9519`, noise-geometry model R2 `0.9943`;
- matched `Delta S`: noise-geometry model R2 `0.9835`, Spearman `0.9777`.

The evidence supports an incremental role for state-dependent noise geometry, especially in matched-system differences and stability prediction. It does not show that leading projected-noise EoS theory fails for absolute sharpness.

## 4. G8.10 mixed-fourth neural branch

The neural branch tests

\[
\chi_{mix}=D^4L[u,u,v,v],
\]

where `u` is the top Hessian eigenvector and `v` is a frozen transverse direction derived from the sharpness gradient.

Estimator feasibility, descriptor replication, and finite-horizon target acquisition were established before the final predictive test.

### B4 primary held-out test

The frozen primary comparison was `N3` (strong lower-order + stochastic + finite-step + rotation baseline) versus `N4=N3+chi_mix`, using fresh seed groups and grouped out-of-fold ridge regression.

Across 30 usable checkpoints from 16 seed groups:

- MAE `2.0926 -> 1.9942`;
- MAE gain `0.04699`, 95% seed-group bootstrap CI `[-0.06188, 0.15109]`;
- `Delta R2 = 0.00325`, CI `[-0.05698, 0.04135]`;
- residual Spearman `0.3277`, CI `[-0.0704, 0.6311]`;
- sign agreement `0.6333`;
- paired permutation `p = 0.0428`.

The preregistered primary verdict is **`FAIL_NO_PRIMARY_NEURAL_INCREMENTAL_VALUE`** because the effect did not meet the frozen magnitude, uncertainty, correlation, sign, and cross-regime robustness gates.

The eta-stratified MAE gain was `+14.76%` at `eta=0.018` but `-2.66%` at `eta=0.020`. This is retained only as exploratory evidence for possible regime dependence.

### Secondary Liao-mechanistic subset

The secondary paper-faithful mechanism test is **inconclusive**. Only 3 independent seed groups survived the exact applicability/moving-reference pipeline; most attrition came from local alpha/beta prerequisite failure after exact KKT projection. This does not constitute evidence against the Liao mechanism itself.

## 5. Higher-order covariance theory

Internal fixed-horizon expansions identify additional local stochastic information beyond additive covariance, including covariance-field derivatives and higher cumulants. These derivations remain mathematically useful, but broad novelty is not claimed because the ingredients overlap stochastic modified equations, weak expansions, B-series, cumulant theory, and multiplicative-noise literature.

The neural B4 result is an important constraint: measurability of a higher-order descriptor does not imply regime-robust predictive value.

## 6. Important negative / narrowing results

- additive zero-mean noise alone does not generically shift the local mean-Jacobian spectrum;
- pure affine non-Gaussian noise can change the transition operator without changing its eigenvalues;
- a universal temporal-covariance closure for iid SGD is not viable under standard filtration assumptions;
- higher cumulants alone are not a defensible novelty claim;
- the preregistered regime-robust neural incremental-value claim for `chi_mix` failed in G8.10-B4;
- the secondary Liao-mechanistic B4 test remains unresolved because of applicability attrition, not because of a confirmed mechanism failure.

## 7. Current priorities

1. Finish the cheap post-hoc diagnostic of the observed eta heterogeneity without changing the B4 verdict.
2. Only if a regime-dependent signal survives influence, residualization, collinearity, and negative-control audits, preregister a small independent confirmatory test.
3. Continue genuine finite-sum/minibatch and multidimensional tests of the stronger M9 noise-geometry result.
4. Keep exact comparison with Liao et al. 2026 and Ignashin et al. 2026 for every new theorem or neural claim.
5. Preserve strict separation between theorem, controlled numerical evidence, exploratory hypotheses, inconclusive tests, and falsified claims.
