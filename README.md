# Finite-Step Stochastic Dynamics of SGD

Research repository studying the temporal stochastic geometry of finite-step stochastic gradient descent (SGD).

**Version:** 1.0.0 (research release, 2026-09-09)

## Overview

This repository investigates whether the temporal organization of SGD stochasticity contains predictive information about finite-step parameter dynamics beyond marginal gradient-noise statistics.

## Core question

Can temporal structure of SGD gradient noise predict finite-horizon stochastic covariance geometry and spectral effects beyond models based only on instantaneous noise statistics?

## Research progression

- **Stage 3I-R:** exact validation of the local Hessian-covariance mechanism.
- **Stage 3J:** residual analysis beyond the validated second-order contribution.
- **Stage 3K:** held-out zero-fit finite-step prediction.
- **M1:** finite-horizon covariance prediction under i.i.d. minibatching.
- **M2:** temporal covariance effects under random reshuffling.
- **M7/T1:** causal temporal-ordering ablations and neural-SGD transfer.

## Reproducibility

The repository contains:

- experiment source code;
- frozen configurations;
- provenance records;
- validated, exploratory, and negative-result archives;
- automated public-release quality checks.

Large raw computational artifacts are intentionally separated from the Git repository.

## Scientific principle

The project follows a falsification-driven workflow. Negative and inconclusive experiments are preserved, and scientific claims are restricted to regimes supported by validation evidence.

## Citation

If you use this repository, please cite the release version specified in `CITATION.cff`.
