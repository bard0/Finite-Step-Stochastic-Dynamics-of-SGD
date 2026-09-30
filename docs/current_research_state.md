# Current Research State

**Frozen state:** 2026-09-30  
**Milestone:** v1.0 complete.

## Final scientific question

Which stochastic information is sufficient to predict a specified finite-step SGD stability or dynamical observable?

The project no longer looks for a universal “extra correction term.” The final framing is descriptor sufficiency / spectral closure for finite-step SGD.

## Final v1 analytical core

### A1. Exact scalar finite-step stability construction

There is an explicit scalar finite-sum SGD construction in which lower-order reference descriptors match while state-dependent stochastic geometry changes the exact second-moment stability boundary:

\[
q=(1-\eta\lambda)^2+\eta^2G_\Sigma,
\qquad
\eta_c=\frac{2\lambda}{\lambda^2+G_\Sigma}.
\]

This is an existence / insufficiency theorem. It does not claim novelty for multiplicative noise or mean-square stability theory.

### A2. Additive control

For \(G_\Sigma=0\), the boundary reduces to \(2/\lambda\). Controlled additive-noise tests likewise do not support a generic physical mean spectral shift from scalar noise amplitude alone.

### A3. iid temporal-covariance correction

For conditionally unbiased independently resampled with-replacement minibatches, centered innovations are martingale differences. A generic nonzero cross-time centered covariance is therefore not a universal iid-SGD memory descriptor.

## Final controlled evidence

### M9

- system-level \(\eta_c\): \(R^2=0.7791\), Spearman \(0.8714\);
- matched \(\Delta\eta_c\): \(R^2=0.8485\), Spearman \(0.9543\);
- absolute sharpness gap: projected-noise baseline \(R^2=0.9519\), noise-geometry model \(R^2=0.9943\);
- matched \(\Delta S\): noise-geometry \(R^2=0.9835\), Spearman \(0.9777\).

Interpretation: state-dependent noise geometry has controlled incremental value, especially in matched-system separation and stability prediction.

## Final neural evidence

The preregistered G8.10-B4 comparison \(N3\) versus \(N4=N3+\chi_{mix}\) did not satisfy the frozen regime-robust success gates.

**Verdict:** `FAIL_NO_PRIMARY_NEURAL_INCREMENTAL_VALUE`.

The eta heterogeneity remains exploratory only. The secondary paper-faithful Liao moving-reference subset remains inconclusive because too few independent seed groups passed the exact applicability pipeline.

## Late theory frontier

Late finite-step proof work produced local matched-information constructions for future sharpness, but also showed where the compact closure breaks down. In particular, coupling quotients derived for frozen stochastic laws expand when the stochastic law moves with time or state.

These results are kept as possible v2 material. They are not used as a general moving-PGD, long-horizon, or neural theorem in v1.

## Final non-claims

v1 does not claim a universal neural SGD spectral law, universal critical batch-size formula, new general state-dependent-noise theory, optimizer improvement, generalization improvement, or a complete long-horizon EoS closure.

## Project status

**v1 is complete.** Moving-reference theory, multidimensional transfer, another prospective neural test, or a theorem-level priority study would start a separate v2.
