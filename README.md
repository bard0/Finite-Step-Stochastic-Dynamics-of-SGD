# Finite-Step Stochastic Dynamics of SGD

This repository contains a completed research project on finite-step stochastic gradient descent.

The work started with a spectral perturbation question: **how does minibatch noise change local SGD dynamics?** Several controls showed that this was too broad. The project eventually narrowed to a more concrete problem:

> **Which stochastic descriptors are sufficient to predict a finite-step stability or dynamical quantity?**

**Status:** v1.0 complete as of 2026-09-30.  
Possible moving-reference, long-horizon, and broader neural extensions are kept separate as future work.

## Main results

### 1. Controlled spectral test

In a stochastic Duffing system, the perturbative spectral predictor agreed closely with directly measured spectral shifts when the assumptions of the approximation were enforced:

- mean absolute error: about (1.5\times10^{-7});
- median relative error: about (2.5\times10^{-3});
- Spearman correlation: about (0.999).

An additive-noise control showed essentially no physical mean spectral shift. This ruled out the simple explanation that noise amplitude alone drives the effect.

### 2. Exact finite-step stability construction

For a scalar finite-sum model,

[
q=(1-etalambda)^2+eta^2G_Sigma,
qquad
eta_c=rac{2lambda}{lambda^2+G_Sigma}.
]

The construction shows that lower-order local descriptors can match while the exact finite-step second-moment stability threshold differs because the noise geometry depends on the state.

The claim is intentionally narrow: this is a descriptor-insufficiency result, not a new general theory of multiplicative noise.

### 3. M9 controlled comparison

| target | simpler baseline | noise-geometry model |
|---|---:|---:|
| system-level (eta_c), (R^2) | -1.2446 | **0.7791** |
| matched A-B (Deltaeta_c), (R^2) | -2.2405 | **0.8485** |
| absolute sharpness gap, (R^2) | 0.9519 | **0.9943** |
| matched A-B (Delta S), (R^2) | -0.1682 | **0.9835** |

The simpler projected-noise model already explains most of the absolute sharpness variation. The additional value of (G_Sigma) is clearest in matched-system differences and stability-threshold prediction.

### 4. Neural higher-order test

The neural branch tested

[
chi_{mix}=D^4L[u,u,v,v]
]

on fresh seed groups against a strong lower-order baseline.

Across 30 checkpoints from 16 seed groups:

- MAE: 2.0926 -> 1.9942;
- pooled MAE gain: 4.70%;
- bootstrap interval for the gain: [-0.0619, 0.1511];
- eta-specific gain: +14.76% at 0.018, -2.66% at 0.020.

The preregistered cross-regime criterion was not met. The primary result is therefore negative. The difference between the two learning-rate regimes is kept as exploratory only.

## Ideas that did not survive

Several hypotheses were useful precisely because they failed:

- additive zero-mean noise as a generic spectral-shift mechanism;
- centered temporal covariance as a universal memory descriptor for ordinary iid SGD;
- simple linear (K_{st}) propagation as a general neural closure;
- operator difference by itself as evidence of spectral difference;
- “higher cumulants matter” as a novelty claim;
- regime-robust incremental value of (chi_{mix}) in G8.10-B4.

These failures are part of the project record and explain why the final question is about descriptor sufficiency rather than a universal stochastic correction.

## Scope

The project does **not** claim:

- a universal spectral law for neural-network SGD;
- a universal critical batch-size formula;
- a new general theory of state-dependent noise;
- a new optimizer or improved generalization;
- a general moving-PGD or long-horizon closure theorem.

## Relation to nearby work

The project is positioned relative to:

- Liao et al. (2026), stochastic sharpness-gap / edge-of-stability dynamics;
- Ignashin et al. (2026), finite-step SGD beyond Brownian closure;
- stochastic modified equations and weak expansions;
- stochastic B-series and cumulant expansions;
- state-dependent / multiplicative noise and mean-square stability theory.

The generic ingredients in those literatures are not claimed as new here.

## Repository map

- [FINAL_RESEARCH_SUMMARY.md](FINAL_RESEARCH_SUMMARY.md) — longer account of the project;
- [PROJECT_FREEZE_v1.md](PROJECT_FREEZE_v1.md) — exact boundary between v1 and possible future work;
- [docs/claims_and_evidence.md](docs/claims_and_evidence.md) — claim/evidence ledger;
- [docs/portfolio_key_results.md](docs/portfolio_key_results.md) — three compact results for talks;
- [research_history/](research_history/) — short history of how the hypotheses changed;
- [experiments/M9/](experiments/M9/) — controlled noise-geometry benchmark;
- [experiments/G8_10/](experiments/G8_10/) — neural higher-order test.

Large checkpoints, raw trajectories, full logs, and canonical archives are kept outside Git.

## Evidence labels

Results are marked as analytical, controlled numerical, exploratory, inconclusive, or negative. A descriptor is only promoted when it has a theorem-level consequence or survives a held-out predictive test.
