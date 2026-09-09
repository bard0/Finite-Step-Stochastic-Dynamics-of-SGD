# M7 — Temporal-ordering causal ablation

## Purpose

M7 tests whether temporal organization of stochastic gradient noise contributes predictive information about finite-horizon stochastic covariance beyond matched one-step marginal statistics.

## Experimental idea

The comparison isolates temporal ordering while controlling marginal noise statistics:

- real temporal ordering;
- temporally shuffled ordering;
- marginally matched independent controls.

The goal is causal identification of the temporal contribution, not merely correlation analysis.

## Interpretation

A successful result supports the statement that temporal organization can affect finite-horizon stochastic covariance geometry in the tested regime.

It does not imply a universal law of SGD or a universal memory mechanism.
