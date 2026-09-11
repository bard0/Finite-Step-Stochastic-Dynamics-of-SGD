# Descriptor Sufficiency for Finite-Step SGD

## Problem

Given the exact finite-step transition law

\[
(P_\eta f)(\theta)=\mathbb E f(\theta-\eta g_B(\theta)),
\]

which compressed local descriptors are sufficient to determine a chosen observable such as mean-square stability, covariance evolution, relaxation, or an EoS statistic?

## Confirmed scalar separation

The project has an explicit finite-sum scalar construction with matched population Hessian and matched zero-order covariance `Sigma(0)` but different multiplicative noise geometry.

For the solvable mean-square recursion,

\[
\mathbb E[x_{t+1}^2]=q\,\mathbb E[x_t^2]+\text{additive term},
\qquad
q=(1-\eta\lambda)^2+\eta^2G_\Sigma.
\]

Hence

\[
\eta_c=\frac{2\lambda}{\lambda^2+G_\Sigma}.
\]

This proves that `(H, Sigma(0))` is not an operator-complete or stability-complete descriptor pair in this class.

## M9 consequence

A frozen predictor using `G_Sigma` predicts both absolute thresholds and matched-system threshold differences substantially better than the zero-order baseline in the controlled 1D family.

## What is not proved

- that `G_Sigma` is a universal sufficient statistic for SGD;
- that it dominates leading projected-noise EoS theory for absolute sharpness;
- that the scalar formula transfers unchanged to deep networks;
- that all relevant state dependence is captured by a single covariance-curvature scalar.

## Stronger hierarchy

The finite-horizon covariance expansion suggests a descriptor hierarchy involving derivatives of the covariance field and higher cumulants. These are useful for approximation closure, but generic higher-order stochastic expansions are established prior art. The research question is therefore sufficiency/minimality for specific SGD observables, not discovery of the tensors themselves.
