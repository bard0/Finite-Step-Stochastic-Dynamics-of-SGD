# Literature Positioning

## Scope of the claim

The project does **not** claim that state-dependent SGD noise, multiplicative noise, higher cumulants, mean-square stability, or finite-step weak expansions are new.

The current candidate contribution is narrower:

> standard low-order local EoS / noise-amplitude descriptors need not be sufficient to determine finite-step mean-square stability; an explicit finite-sum construction and controlled comparison isolate a state-dependent noise-geometry term with a measurable stability consequence.

## Primary comparators

### Liao et al. (2026) — stochastic sharpness gap

Liao et al. provide a leading-order EoS description involving curvature/nonlinear stabilization and projected gradient-noise variance. This repository treats that framework as a baseline, not an opponent.

M9 is consistent with this distinction: the projected-noise model already explains most of the absolute sharpness gap, while the additional noise-geometry descriptor is most visible in matched-system differences and threshold prediction.

### Ignashin et al. (2026) — finite-step discrete SGD

Ignashin et al. motivate starting from the discrete SGD transition law rather than assuming a Brownian closure. The present project shares that finite-step viewpoint but asks a different question: which compressed stochastic descriptors retain enough information for stability and prediction?

## Adjacent established areas

Any novelty statement must be checked against:

- stochastic modified equations and weak approximations of SGD;
- Talay–Tubaro / stochastic B-series expansions;
- Kramers–Moyal and higher-cumulant descriptions;
- multiplicative-noise and state-dependent diffusion theory;
- stochastic approximation and mean-square stability of random linear systems;
- random reshuffling / without-replacement SGD;
- Hessian-aware stochastic dynamics and local stability analyses.

## Safe wording

Appropriate:

- "descriptor insufficiency";
- "explicit finite-sum realization";
- "finite-step mean-square stability consequence";
- "controlled incremental predictive value in the tested family".

Avoid:

- "first state-dependent-noise theory of SGD";
- "SGD is not Brownian" as a project novelty;
- "higher cumulants are a new SGD mechanism";
- "projected-noise EoS theory is wrong";
- "universal spectral theory of SGD".

## Current novelty assessment

The exact scalar counterexample plus controlled M9 evidence is a credible focused contribution. The broader higher-order covariance-jet hierarchy is mathematically interesting but heavily adjacent to established stochastic-numerics machinery; priority and publication novelty remain unresolved.
