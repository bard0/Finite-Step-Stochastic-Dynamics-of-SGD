# M1 — finite-horizon covariance prediction

## Research question

Can local gradient-noise covariance together with deterministic tangent propagation predict finite-horizon stochastic covariance geometry of SGD?

## Mathematical object

The experiment studies the propagation of temporal covariance structure into a finite-horizon covariance observable:

\[
C_H = \eta^2 \sum_{s,t} P_{s,H} K_{st} P_{t,H}^{T}.
\]

The comparison is against descriptions that retain only marginal one-step noise statistics.

## Current interpretation

M1 provides evidence that finite-horizon covariance evolution contains information beyond a scalar noise magnitude description in the tested regime.

The result is intentionally limited to the evaluated models, observables and experimental conditions.

## Public artifact policy

The repository should contain:

- configuration files;
- exact archived execution scripts when available;
- compact summary tables;
- provenance information.

Large generated tensors and raw trajectories remain external artifacts.
