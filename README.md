# Finite-Step Stochastic Dynamics of SGD

Research repository for finite-step stochastic gradient descent (SGD), with emphasis on stability, state-dependent gradient-noise geometry, higher-order local descriptors, and falsification-first neural transfer tests.

**Research state:** 2026-09-15

## Current scientific focus

The project asks which stochastic descriptors are sufficient to predict finite-step SGD stability and edge-of-stability observables.

The exact one-step object is

\[
(P_\eta f)(\theta)=\mathbb E\,f(\theta-\eta g_B(\theta)).
\]

For local mean-square stability, lifted second-moment dynamics remain central. For neural transfer, the current question is whether higher-order local geometry adds held-out predictive information beyond lower-order stochastic, curvature, finite-step, and eigenspace-rotation descriptors.

## Strongest analytical result

A controlled scalar finite-sum construction shows that two SGD systems can share the same population Hessian and the same zero-order gradient-noise covariance at the reference point while having different exact finite-step second-moment stability thresholds.

For the exactly solvable multiplicative-noise model,

\[
q=(1-\eta\lambda)^2+\eta^2 G_\Sigma,
\qquad
\eta_c=\frac{2\lambda}{\lambda^2+G_\Sigma}.
\]

The contribution is an explicit descriptor-insufficiency statement and finite-step stability consequence, not the generic observation that state-dependent noise exists.

## M9 controlled comparison

`experiments/M9/` contains the compact public record of the controlled EoS comparison.

| target | baseline | noise-geometry model |
|---|---:|---:|
| system-level `eta_c` R2 | -1.2446 | **0.7791** |
| matched A-B `Delta eta_c` R2 | -2.2405 | **0.8485** |
| system-level sharpness-gap R2 | 0.9519 | **0.9943** |
| matched A-B `Delta S` R2 | -0.1682 | **0.9835** |

The projected-noise baseline already explains most of the absolute sharpness gap. The stronger evidence for `G_Sigma` is in matched-system separation and stability-threshold prediction.

## G8.10 neural mixed-fourth transfer test

The neural branch studies the mixed fourth directional derivative

\[
\chi_{mix}=D^4L[u,u,v,v],
\]

with `u` the top Hessian eigenvector and `v` a frozen transverse direction derived from the sharpness gradient.

Estimator feasibility and target acquisition were established before the final held-out test. The preregistered B4 comparison then asked whether adding `chi_mix` to the strongest frozen lower-order/rotation baseline improved future sharpness prediction across two sustained-EoS regimes.

Primary B4 result (`N3 -> N4`, 30 checkpoints, 16 seed groups):

- MAE: `2.0926 -> 1.9942` (`+4.70%` gain);
- R2: `0.71795 -> 0.72120` (`Delta R2 = 0.00325`);
- residual Spearman: `0.3277`;
- sign agreement: `0.6333`;
- seed-group bootstrap CI for MAE gain: `[-0.0619, 0.1511]`;
- paired permutation `p = 0.0428`.

The preregistered regime-robust incremental-value claim **failed**. The effect was heterogeneous across `eta`: `+14.76%` MAE gain at `eta=0.018` versus `-2.66%` at `eta=0.020`. This heterogeneity is exploratory and is not treated as confirmation.

The paper-faithful Liao-mechanistic subset remained inconclusive because too few independent seed groups survived the exact applicability/moving-reference pipeline.

See `experiments/G8_10/` for the compact public record.

## Theory status

Two main theory tracks are retained:

1. **Noise-geometry / descriptor sufficiency.** Which local stochastic descriptors are required for finite-step stability and observable dynamics?
2. **Higher-order finite-horizon geometry.** Which higher derivatives/cumulants can matter beyond additive-covariance closures, and which survive held-out predictive tests?

Broad novelty claims are avoided where the ingredients overlap stochastic modified equations, weak expansions, B-series, cumulant expansions, and multiplicative-noise theory.

## Literature boundary

The project is positioned relative to:

- Liao et al. (2026), stochastic sharpness-gap / EoS dynamics;
- Ignashin et al. (2026), discrete finite-step SGD beyond Brownian closure;
- stochastic modified-equation and weak-expansion literature;
- state-dependent / multiplicative gradient-noise theory;
- stochastic approximation and mean-square stability theory.

## Evidence policy

Claims are tagged as analytical, controlled numerical, exploratory, inconclusive, or falsified. Negative results are preserved. A measurable descriptor is not promoted unless it produces a reproducible observable or held-out predictive consequence.

## Repository map

- `docs/current_research_state.md` — current state and strongest claims;
- `docs/claims_and_evidence.md` — claim ledger;
- `docs/theory/` — theory notes and limitations;
- `experiments/` — compact public experiment records;
- `paper/` — manuscript outline and evidence roadmap.

Large checkpoints, full logs, archives, and canonical experiment records remain in the project archive and are not duplicated in Git.
