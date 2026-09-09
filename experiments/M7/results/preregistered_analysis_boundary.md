# M7 preregistered analysis boundary

## Research question

Does the temporal organization of stochastic-gradient noise provide predictive information about finite-horizon stochastic dynamics beyond marginal noise statistics?

## Comparisons

Mode A uses the recorded natural ordering. Mode B replays exactly the same recorded noise vectors in a random temporal permutation. Mode C replays an IID Gaussian surrogate fitted to A's empirical mean and covariance model. B and C are counterfactual frozen-noise replays using the same initialization, dataset, full-gradient update, learning rate, and horizon; they are not new minibatch-SGD runs.

## Confirmation pattern

The hypothesis is supported only if pre-outcome checks show exact A/B sample preservation and materially reduced off-diagonal temporal covariance in B/C, and if a prespecified finite-horizon metric consistently differs between A and B while a full temporal-K prediction improves on the K0-only prediction. The experiment program reports quantities only; it makes no automated support claim.

## Falsification pattern

The hypothesis is not supported for a condition if A, B, and C agree within seed variability, if rho=0 does not yield approximate A/B/C agreement, if differences track only trace(Sigma), if distribution/covariance checks fail, or if any apparent effect is seed-specific.

## Alternative explanations

Finite sample error, replay mismatch away from the recorded path, non-Gaussianity in C, inadequate seed count, unstable nonlinear local response, optimizer implementation effects, and insufficient horizon are alternatives. EDMD/Koopman spectra are diagnostics only and cannot establish causation.

## Experimental design

M7.1 uses a stable diagonal linear system with eigenvalues 0.95, 0.8, 0.5, 0.2 and AR(1) noise at rho=0 and rho=0.75. M7.2 uses a frozen 10-32-32-1 ReLU MLP, synthetic regression data of size 512, batch sizes 8/16/32/64/128, learning rates 0.01/0.005, and five fixed seeds. Horizons are 10/25/50/100.

## Statistical analysis

No post-hoc hypothesis test or automatic verdict is run. Seed-level outputs are intended for a preregistered paired analysis keyed by `(learning_rate, batch_size, seed, horizon, projection)`.

## Permitted interpretation

If later warranted by independent analysis, interpretation is limited to: temporal organization of stochastic-gradient noise provides additional predictive information about finite-horizon stochastic dynamics beyond marginal noise statistics.

## Current overall status

**UNDECIDED.** The experiment program itself does not calculate, select, or state a scientific verdict for the full M7 program.
