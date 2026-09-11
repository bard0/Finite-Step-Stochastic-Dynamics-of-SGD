# Finite-Step Stochastic Dynamics of SGD

Research repository studying finite-step stochastic gradient descent (SGD) as a discrete stochastic dynamical system.

**Version:** 1.1.0 (research state update, 2026-09)

## Overview

The project investigates which stochastic information determines finite-horizon SGD dynamics beyond classical instantaneous gradient-noise descriptors.

## Core questions

1. Can temporal organization of SGD stochasticity predict finite-step covariance and spectral behavior beyond matched marginal statistics?

2. Are common edge-of-stability descriptors sufficient to characterize finite-step SGD dynamics?

3. Where do discrete SGD dynamics differ from continuous stochastic approximations?

## Research progression

- Controlled validation of local stochastic covariance mechanisms.
- Finite-horizon covariance prediction under stochastic minibatching.
- Temporal ordering and causal ablation experiments.
- Neural-SGD transfer studies.
- Finite-step operator and descriptor insufficiency theory.

## Theoretical viewpoint

The project studies the exact finite-step transition operator:

\[
P_\eta f(\theta)=E[f(\theta-\eta g_B(\theta))]
\]

rather than assuming that SGD is fully described by a continuous diffusion approximation.

## Reproducibility

The repository contains:

- experiment source code;
- configurations;
- provenance records;
- validated, exploratory, and negative-result archives;
- public release quality checks.

Large computational artifacts remain separated from source control.

## Scientific principle

The workflow is falsification-driven. Negative and inconclusive results are preserved, and claims are limited to regimes supported by evidence.

## Citation

If you use this repository, cite the release specified in `CITATION.cff`.
