# Current Research State

## Research direction

The project studies finite-step stochastic gradient descent (SGD) as a discrete stochastic dynamical system rather than only as a continuous Langevin approximation.

## Current central hypothesis

Classical stochastic descriptors and edge-of-stability descriptors may be insufficient to determine finite-step SGD spectral and covariance dynamics.

The working question is:

> Which stochastic information is required to predict finite-horizon SGD dynamics beyond instantaneous gradient-noise statistics?

## Current theoretical line

The finite-step SGD transition operator is considered directly:

P_eta f(theta) = E[f(theta - eta g_B(theta))]

The project investigates when different stochastic processes with matched low-order descriptors generate different finite-step operators.

## Relation to recent work

The project is positioned relative to:

- analyses of stochastic sharpness and edge-of-stability behavior;
- discrete stochastic dynamics of SGD;
- stochastic modified equations;
- Langevin approximations.

Recent work by Liao et al. and Ignashin et al. motivates separating observable training descriptors from the full discrete stochastic dynamics.

## Evidence status

- Confirmed: controlled experiments validating specific finite-step stochastic effects.
- Exploratory: descriptor insufficiency hypotheses requiring further validation.
- Open: rigorous characterization of minimal sufficient stochastic descriptors.
