# Current Research State

## Research direction

The project studies finite-step stochastic gradient descent (SGD) as a discrete stochastic dynamical system rather than only as a continuous Langevin approximation.

## Current central hypothesis

The strongest surviving hypothesis is not that SGD has universal memory or that a single covariance closure describes SGD. The current question is whether finite-step SGD behavior requires richer predictive observables than classical marginal descriptors.

Working hypothesis:

> Early finite-step stochastic observables can contain predictive information about future SGD dynamics beyond Gradient Noise Scale, marginal covariance, and Hessian/sharpness diagnostics.

## Current theoretical line

The exact finite-step transition operator remains the mathematical object:

P_eta f(theta) = E[f(theta - eta g_B(theta))]

However, broad operator/spectral claims are not the main contribution. The current goal is to identify minimal sufficient observables or rigorous approximation-validity criteria.

## Major corrections after audits

- Temporal covariance K_st is no longer treated as a universal missing descriptor.
- Simple second-order covariance closure was not sufficient in neural SGD validation.
- Random reshuffling temporal effects remain relevant but have strong prior art and are not the main novelty target.
- Theoretical validity certificates are retained as a possible contribution, but require sharpness analysis against existing high-Lp and stochastic approximation results.

## Current branches

### Predictive SGD dynamics

Primary empirical direction:
- compare GNS;
- Hessian/sharpness diagnostics;
- marginal covariance;
- temporal/state-dependent stochastic observables;
- approximation error prediction.

### Finite-step theory

Primary theoretical direction:
- exact discrete operator expansion;
- finite-horizon approximation validity;
- separation of additive covariance, multiplicative Hessian noise, and nonlinear remainder terms.

## Evidence status

- Confirmed: controlled finite-step stochastic effects and validated local mechanisms.
- Exploratory: predictive observable discovery and descriptor insufficiency.
- Open: minimal sufficient stochastic description of finite-step SGD.
