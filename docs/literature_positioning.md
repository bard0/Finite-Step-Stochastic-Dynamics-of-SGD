# Literature positioning

## Scope

The repository studies temporal stochastic geometry of finite-step SGD. The contribution is not the existence of stochastic effects in SGD, but whether temporal organization of gradient noise provides additional predictive information for finite-horizon covariance dynamics beyond matched marginal statistics.

## Relation to prior directions

### Curvature and gradient-noise analyses

Existing work studies projected gradient noise, Hessian interactions, and local stochastic dynamics. This project extends the question toward temporal covariance structure.

### Finite-step SGD dynamics

Discrete SGD corrections beyond continuous diffusion approximations are an established research direction. The focus here is empirical zero-fit prediction of finite-horizon stochastic quantities.

### Random reshuffling

Without-replacement sampling and temporal dependence are established topics. The repository does not claim discovery of random reshuffling effects; it tests whether their temporal structure improves covariance prediction.

## Positioning against recent SGD work

The project should be compared explicitly with recent finite-step and stochastic-dynamics analyses, including Liao et al. (2026) and Ignashin et al. (2026), while keeping claims restricted to experimentally supported regimes.

## Core distinction

The central object is:

`K_st = Cov(xi_s, xi_t)`

and its contribution to:

`C_H = eta^2 sum P_s,H K_st P_t,H^T`

rather than scalar noise magnitude alone.
