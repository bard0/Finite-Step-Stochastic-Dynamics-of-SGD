# M7 — temporal-ordering causal ablation

## Purpose

M7 tests whether temporal organization of stochastic-gradient noise contributes predictive information about finite-horizon stochastic dynamics beyond matched one-step marginal statistics.

## Causal comparison

The design separates three replay modes:

- **A — real order:** recorded natural ordering;
- **B — shuffled order:** exactly the same recorded noise vectors under a random temporal permutation;
- **C — IID matched control:** an independent surrogate matched to the empirical one-step mean/covariance model.

A and B therefore preserve the per-coordinate noise samples while changing temporal organization.

## Controlled M7.1 linear evidence

For the correlated-noise condition (`rho = 0.75`), A/B one-step samples are preserved to numerical precision while the measured off-diagonal temporal covariance norm changes strongly:

- real: `2.2655903266`;
- shuffled: `0.5322192625`;
- IID control: `0.6357297323`.

The corresponding empirical finite-horizon covariance traces are:

- real: `75.7185958635`;
- shuffled: `39.5412860194`;
- IID control: `43.7537584176`.

The full temporal predictor has relative Frobenius error `0.0615037862` for the real-order condition in this controlled linear case.

At `rho = 0`, off-diagonal temporal covariance is small in all three modes, providing the intended null-control regime.

## Interpretation boundary

These results constitute controlled evidence that temporal ordering can change finite-horizon covariance geometry when one-step samples are matched in the **M7.1 linear system**.

They do not by themselves establish the neural-SGD result, a universal memory mechanism, or a universal law of SGD.

## Overall M7 status

**UNDECIDED.** The preregistered M7 program does not automatically issue a scientific verdict. The neural-SGD component and paired cross-condition analysis must be assessed before promoting the full M7 hypothesis.
