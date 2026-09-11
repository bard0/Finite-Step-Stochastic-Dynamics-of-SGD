# Finite-Step Stochastic Dynamics of SGD

Research repository for finite-step stochastic gradient descent (SGD), with emphasis on stability, state-dependent gradient-noise geometry, and the limits of low-order stochastic descriptors.

**Research state:** 2026-09-12

## Current scientific focus

The project has moved away from a broad claim of a universal spectral/Koopman theory of SGD. The current core question is narrower:

> Which stochastic descriptors are sufficient to predict finite-step SGD stability and related edge-of-stability observables?

The exact one-step object is the SGD transition operator

\[
(P_\eta f)(\theta)=\mathbb E\,f(\theta-\eta g_B(\theta)).
\]

For local mean-square stability, the corresponding lifted second-moment dynamics are central.

## Strongest current result

A controlled scalar finite-sum construction shows that two SGD systems can share the same population Hessian and the same zero-order gradient-noise covariance at the reference point while having different exact finite-step second-moment stability thresholds.

For the exactly solvable multiplicative-noise model,

\[
q=(1-\eta\lambda)^2+\eta^2 G_\Sigma,
\]

and the mean-square boundary is

\[
\eta_c=\frac{2\lambda}{\lambda^2+G_\Sigma}.
\]

Here `G_Sigma` is a local noise-geometry term (zero for the additive-noise control). The contribution is **not** that state-dependent noise exists; that is established prior art. The candidate contribution is the descriptor-insufficiency framing, explicit finite-sum realization, and finite-step stability consequence.

## M9 controlled comparison

`experiments/M9/` contains the saved text/tabular artifacts from the controlled EoS comparison.

Key frozen-predictor results:

| target | baseline | noise-geometry model |
|---|---:|---:|
| system-level `eta_c` R2 | -1.2446 | **0.7791** |
| matched A-B `Delta eta_c` R2 | -2.2405 | **0.8485** |
| system-level sharpness-gap R2 | 0.9519 (projected-noise model) | **0.9943** |
| matched A-B `Delta S` R2 | -0.1682 | **0.9835** |

The absolute sharpness result is important for claim discipline: the projected-noise baseline already explains most of the system-level sharpness gap. The stronger evidence for `G_Sigma` is the matched-system separation and stability-threshold prediction.

## Theory status

Two theory tracks are retained:

1. **Noise-geometry / descriptor sufficiency.** Determine which local stochastic descriptors are required for finite-step stability and observable dynamics.
2. **Higher-order finite-horizon covariance jets.** Internal derivations identify covariance-field derivatives and higher cumulants at orders beyond the additive-covariance approximation. These are mathematically useful, but broad novelty claims are explicitly avoided because stochastic modified equations, weak expansions, B-series, cumulant expansions, and state-dependent diffusion are established literature.

## Literature boundary

The project is positioned relative to, not as a replacement for:

- Liao et al. (2026), *SGD at the Edge of Stability: The Stochastic Sharpness Gap* — leading-order EoS description using curvature and projected gradient-noise variance.
- Ignashin et al. (2026), *Why SGD is not Brownian Motion: A New Perspective on Stochastic Dynamics* — finite-step discrete SGD beyond a Brownian/Langevin closure.
- stochastic modified-equation and weak-expansion literature;
- state-dependent / multiplicative gradient-noise theory;
- stochastic approximation and mean-square stability theory.

## Evidence policy

Claims are tagged as analytical, controlled numerical, exploratory, or falsified. Negative results are preserved. Operator differences are not treated as sufficient evidence unless they produce a measurable stability, spectral, relaxation, or predictive consequence.

## Repository map

- `docs/current_research_state.md` — current state and strongest claims.
- `docs/claims_and_evidence.md` — claim ledger.
- `docs/theory/` — theory notes and limitations.
- `experiments/` — public experiment summaries and compact artifacts.
- `paper/` — current manuscript outline and evidence roadmap.

Large checkpoints, full logs, archives, and canonical experiment records remain on the project Drive and are not duplicated in Git.
