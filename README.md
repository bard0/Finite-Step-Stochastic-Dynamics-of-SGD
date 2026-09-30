# Finite-Step Stochastic Dynamics of SGD

A falsification-driven research project on **which stochastic information is actually needed to predict finite-step SGD stability and dynamics**.

**Project status:** **v1.0 frozen — 2026-09-30**  
The exploratory/theoretical portfolio phase is complete. Publication-oriented extensions are separated into a possible v2.

## Problem

SGD is often compressed into deterministic drift plus a small number of noise statistics. That is useful, but it raises a precise question:

> **Which stochastic descriptors are sufficient for a finite-step SGD observable or stability boundary?**

The mature project starts from the exact Markov/Koopman operator

\[
(P_\eta f)(\theta)=\mathbb E\,f(\theta-\eta g_B(\theta))
\]

and tests increasingly rich closures against analytical counterexamples, controlled benchmarks, and held-out neural experiments.

## Approach

The project combined:

- local spectral perturbation theory;
- solvable stochastic dynamical systems;
- exact finite-step / second-moment analysis;
- state-dependent gradient-noise geometry;
- controlled matched-system benchmarks;
- causal and grouped held-out neural tests;
- explicit negative controls and preregistered stop rules;
- literature comparison against EoS and finite-step SGD theory.

The project deliberately preserved failed hypotheses.

## Key results

### 1. Controlled spectral validation

Early controlled Duffing experiments showed that the perturbative spectral machinery can be extremely accurate when its assumptions are enforced: mean absolute error about \(1.5\times10^{-7}\), median relative error about \(2.5\times10^{-3}\), and Spearman correlation about \(0.999\).

An additive-noise control simultaneously showed that **noise amplitude alone is not a generic spectral-shift mechanism**.

### 2. Exact finite-step stability counterexample

A scalar finite-sum construction matches lower-order reference descriptors while changing exact mean-square stability through state-dependent noise geometry:

\[
q=(1-\eta\lambda)^2+\eta^2G_\Sigma,
\qquad
\eta_c=\frac{2\lambda}{\lambda^2+G_\Sigma}.
\]

This is a descriptor-insufficiency result, not a claim that multiplicative noise or mean-square stability theory are new.

### 3. M9 controlled prediction

| target | simpler baseline | noise-geometry model |
|---|---:|---:|
| system-level \(\eta_c\), \(R^2\) | -1.2446 | **0.7791** |
| matched A-B \(\Delta\eta_c\), \(R^2\) | -2.2405 | **0.8485** |
| absolute sharpness gap, \(R^2\) | 0.9519 | **0.9943** |
| matched A-B \(\Delta S\), \(R^2\) | -0.1682 | **0.9835** |

The strongest evidence for the extra descriptor is in **matched-system separation and stability prediction**. The simpler projected-noise baseline already explains most absolute sharpness variation.

### 4. Neural falsification result

The mixed fourth directional derivative

\[
\chi_{mix}=D^4L[u,u,v,v]
\]

was measurable and passed engineering/estimation gates, but failed the frozen regime-robust held-out success criteria.

Across 30 checkpoints / 16 seed groups:

- MAE: `2.0926 -> 1.9942`;
- pooled gain: `4.70%`;
- bootstrap CI: `[-0.0619, 0.1511]`;
- eta-specific gain: `+14.76%` at `0.018`, `-2.66%` at `0.020`.

**Final verdict:** `FAIL_NO_PRIMARY_NEURAL_INCREMENTAL_VALUE`.

This negative result is part of the contribution: a measurable high-order descriptor was not post-hoc promoted after failing the preregistered robustness gates.

## What failed — and changed the project

- generic additive noise as the main spectral mechanism;
- a universal centered temporal-covariance “memory” mechanism for ordinary iid SGD;
- simple linear \(K_{st}\) propagation as a universal neural predictive closure;
- operator difference as sufficient evidence of spectral difference;
- “higher cumulants matter” as a novelty claim;
- regime-robust neural incremental value of \(\chi_{mix}\).

Each failure narrowed the final question from “find a new stochastic effect” to **identify the information needed for a specified finite-step observable**.

## Final conclusion

Finite-step SGD dynamics cannot, in general, be summarized by one scalar noise amplitude or by an unqualified low-order stochastic closure.

Controlled models show that **state-dependent stochastic geometry can change stability and matched-system behavior**. Neural transfer tests simultaneously show that **adding more sophisticated local descriptors does not automatically improve robust prediction**.

The v1 outcome is therefore a map of **successful, insufficient, and falsified stochastic descriptions of SGD**, rather than one universal formula.

## Literature boundary

The project is positioned relative to:

- **Liao et al. (2026):** stochastic sharpness-gap / edge-of-stability dynamics;
- **Ignashin et al. (2026):** finite-step SGD beyond Brownian closure;
- stochastic modified equations and weak expansions;
- stochastic B-series and cumulant expansions;
- state-dependent / multiplicative gradient-noise and mean-square stability theory.

Broad novelty is not claimed for ingredients that already exist in these literatures.

## Repository map

- [`FINAL_RESEARCH_SUMMARY.md`](FINAL_RESEARCH_SUMMARY.md) — complete v1 narrative;
- [`PROJECT_FREEZE_v1.md`](PROJECT_FREEZE_v1.md) — exact freeze boundary and v2 separation;
- [`docs/claims_and_evidence.md`](docs/claims_and_evidence.md) — evidence ledger;
- [`docs/portfolio_key_results.md`](docs/portfolio_key_results.md) — three recommended portfolio visuals;
- [`research_history/`](research_history/) — compressed research-history map;
- [`experiments/M9/`](experiments/M9/) — controlled noise-geometry benchmark;
- [`experiments/G8_10/`](experiments/G8_10/) — neural higher-order falsification test.

Large checkpoints, complete proof logs, raw trajectories, and canonical archives remain in project storage rather than being duplicated in Git.

## Evidence policy

Claims are separated into **analytical**, **controlled numerical**, **exploratory**, **inconclusive**, and **falsified**. A descriptor is not promoted merely because it is measurable or correlated; it must survive a stated theorem or held-out predictive test.
