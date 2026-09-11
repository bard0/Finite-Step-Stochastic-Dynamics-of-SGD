# Literature positioning

## Scope

The repository studies finite-step stochastic dynamics of SGD as a discrete stochastic dynamical system.

The central question is not whether stochasticity influences SGD, which is established, but whether finite-step dynamics contain predictive and mechanistic information beyond classical descriptors such as local curvature and marginal gradient-noise statistics.

## Relation to prior directions

### Curvature and gradient-noise analyses

Existing work studies projected gradient noise, Hessian interactions, sharpness, and local stochastic dynamics. This project investigates whether these descriptors provide a sufficient description of finite-step stochastic evolution.

### Diffusion and stochastic modified equation approaches

Continuous approximations provide useful asymptotic descriptions. The current direction focuses on identifying regimes where discrete finite-step effects cannot be reduced to diffusion-level statistics.

### Random reshuffling and temporal dependence

Temporal dependence is an established phenomenon. The project tests whether temporal organization carries additional predictive information after matching marginal statistics.

## Positioning against recent SGD work

The project should be compared explicitly with recent analyses of SGD stochastic dynamics, including Liao et al. (2026) and Ignashin et al. (2026), while restricting claims to experimentally and theoretically supported regimes.

## Core distinction

The central object is the finite-step stochastic operator:

`P_eta f(theta) = E[f(theta - eta g_B(theta))]`

rather than only scalar noise magnitude or diffusion coefficients.

A key open problem is whether commonly used descriptors form a sufficient statistic for this operator.
