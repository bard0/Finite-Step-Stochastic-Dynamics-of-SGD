# Paper Outline — Noise Geometry and Finite-Step SGD Stability

## 1. Motivation

Leading local EoS descriptions use curvature and projected gradient-noise magnitude. Ask whether these low-order local descriptors determine finite-step stochastic stability.

## 2. Exact finite-sum counterexample

Construct matched finite-sum SGD systems with equal population Hessian and equal zero-order gradient-noise covariance but different state-dependent noise geometry.

Derive

\[
q=(1-\eta\lambda)^2+\eta^2G_\Sigma,
\qquad
\eta_c=2\lambda/(\lambda^2+G_\Sigma).
\]

## 3. Descriptor-insufficiency statement

Formulate the result as an existence theorem: `(H, Sigma(0))` and analogous zero-order EoS descriptors are not, in general, sufficient statistics for finite-step mean-square stability.

## 4. Controlled M9 comparison

Use frozen predictors and disjoint EST/EVAL seeds. Report system-level and matched A-B threshold/sharpness metrics.

Emphasize that the projected-noise baseline remains strong for the absolute sharpness gap; the incremental value of `G_Sigma` is strongest in matched differences and threshold prediction.

## 5. Multidimensional extension

Present the exact quadratic-Lyapunov drift and the noise-geometry LMI. Clearly distinguish theorem from conjectured neural relevance.

## 6. Neural transfer stress test

Report G8.10 as a falsification-oriented extension, not as support for the main theorem.

- `chi_mix = D^4L[u,u,v,v]` is measurable in the tested smooth neural setup.
- The preregistered B4 pooled held-out `N3 -> N4` test fails the strong regime-robust incremental-value claim.
- Eta-specific heterogeneity is exploratory only.
- The paper-faithful Liao-mechanistic subset is inconclusive because of applicability/moving-reference attrition.

This section is useful because it limits overgeneralization from the controlled scalar theory to neural SGD.

## 7. Relation to prior work

Position relative to stochastic EoS, discrete finite-step SGD, stochastic modified equations, multiplicative-noise stability, and weak stochastic expansions.

## 8. Limitations

- strongest positive evidence is still controlled/low-dimensional;
- no claim that `G_Sigma` is universally sufficient;
- neural mixed-fourth transfer did not pass the preregistered regime-robust test;
- higher-order covariance jets have substantial prior-art overlap;
- secondary Liao attribution is unresolved in the tested neural cohort.

## 9. Next falsification experiments

Genuine finite-sum minibatch replication, multidimensional noncommuting controls, and only narrowly preregistered neural follow-up hypotheses that survive cheap diagnostics.
