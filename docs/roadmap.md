# Research roadmap

## Current priority

1. Establish predictive baseline hierarchy for future SGD behavior.
2. Run falsification-first experiments comparing existing diagnostics and new observables.
3. Develop finite-step approximation validity theory with explicit literature boundaries.
4. Validate surviving mechanisms with causal controls.
5. Prepare theorem-level and experiment-level evidence tables.

## Current empirical direction

The project moved from descriptive stochastic geometry toward predictive SGD dynamics.

Main question:

Can measurable early-training stochastic observables predict future SGD behavior beyond existing diagnostics?

Required baselines:

- Gradient Noise Scale;
- marginal covariance statistics;
- Hessian/sharpness indicators;
- eta*lambda_max stability measures;
- finite-step approximation baselines.

## Current experiment program

### P0 — Baseline Predictability Screen

Determine whether future SGD behavior is predictable and establish the strongest existing baseline before introducing complex observables.

### P1 — Incremental Temporal Structure

Test whether compact temporal features improve held-out prediction beyond marginal/Hessian baselines.

### P2 — State-dependent Noise Geometry

Test whether local variation of the noise field contains additional predictive information.

### P3 — Clean Causal Temporal Intervention

Use matched marginal controls to test causal relevance of cross-time stochastic structure.

### P4 — Nonlinear Residual Audit

Explain why linear covariance closures fail while nonlinear stochastic effects remain observable.

## Theory branch

Priority:

- exact finite-step operator analysis;
- finite-horizon expansion;
- validity boundary of covariance/Hessian approximations;
- explicit comparison with stochastic modified equations and existing SGD theory.

## Claim discipline

Forbidden without new evidence:

- SGD has memory;
- universal stochastic geometry;
- universal spectral law;
- new optimizer claims.

A negative result that eliminates an attractive but unsupported explanation is retained as a successful scientific outcome.
