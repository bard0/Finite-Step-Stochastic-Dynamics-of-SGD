# Finite-Step Operator View

## Motivation

The project studies SGD from the exact discrete update rule:

\[
\theta_{k+1}=\theta_k-\eta g_B(\theta_k)
\]

rather than starting from a continuous diffusion approximation.

## Transition operator

For an observable f:

\[
P_\eta f(\theta)=E[f(\theta-\eta g_B(\theta))]
\]

The research question is whether common stochastic descriptors are sufficient to reconstruct relevant properties of this operator.

## Main hypothesis

Different stochastic processes can share low-order descriptors while producing different finite-step operators and different spectral behavior.

## Research status

This is an active theoretical direction. Claims remain restricted to experimentally validated regimes.
