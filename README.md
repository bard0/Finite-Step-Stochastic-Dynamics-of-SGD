# Finite-Step Stochastic Dynamics of SGD

Research repository for a sequence of falsification-driven experiments on finite-step stochastic gradient descent.

## What is in this repository

The public release contains exact archived experiment scripts plus compact reproducibility artifacts for:

1. exact Hessian-vector validation of the second-order finite-step mechanism;
2. the residual test beyond that mechanism;
3. held-out zero-fit finite-step prediction;
4. finite-horizon covariance prediction under i.i.d. minibatching;
5. summary results for the subsequent random-reshuffling covariance experiment.

## Main current direction

The strongest supported research object is **finite-horizon stochastic covariance geometry**, rather than a universal Koopman/spectral closure claim.

In the tested regimes, the project asks whether

`local gradient-noise covariance + deterministic tangent propagation`

predicts stochastic function-space dynamics without condition-specific fitting.

## Layout

```text
experiments/   exact archived execution scripts
results/       compact decisions, configs, tables and audit summaries
docs/          scientific status, claims, positioning and reproducibility
scripts/       repository validation utilities
```

## Running the archived experiments

The exact scripts are preserved for provenance. Several were designed as Google Colab single-cell programs and contain `/content` paths and optional Drive mounting.

For repository validation:

```bash
python scripts/check_public_release.py
python -m compileall experiments
```

or:

```bash
make check
```

## Data policy

Large raw arrays, checkpoints and multi-gigabyte archives are not committed to Git. See `ARTIFACTS.md`.

## Scope

The repository intentionally keeps negative and inconclusive stages. A failed scientific gate is treated as part of the research record rather than removed from history.
