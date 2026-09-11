# Current Research State

Last synchronized with the project Drive: **2026-09-12**.

## 1. Current question

The project asks which stochastic information is required to predict finite-step SGD behavior near stability boundaries.

The earlier temporal-covariance hypothesis was materially narrowed. For standard iid/with-replacement minibatch SGD, centered innovations form a martingale-difference sequence under the usual conditional-unbiasedness assumptions, so generic off-diagonal temporal covariance is not the missing universal mechanism. Random reshuffling remains a separate sampling regime with genuine temporal structure and substantial prior art.

The primary active SGD mechanism is therefore **state-dependent / multiplicative stochastic geometry** and its finite-step consequences.

## 2. Confirmed mathematical core

### Scalar descriptor-insufficiency counterexample

There is an explicit finite-sum construction in which two systems share the same population objective locally, the same population Hessian `H`, and the same zero-order gradient-noise covariance `Sigma(0)`, but differ in state-dependent noise geometry and in the exact finite-step mean-square stability boundary.

For the solvable scalar model,

\[
q=(1-\eta\lambda)^2+\eta^2 G_\Sigma,
\]

and stability requires `q < 1`, giving

\[
\eta_c=\frac{2\lambda}{\lambda^2+G_\Sigma}.
\]

The additive control has `G_Sigma=0` and recovers `2/lambda`.

This is an **existence / insufficiency** statement. It is not a claim that multiplicative noise, state-dependent covariance, or mean-square stability theory is new.

## 3. M9 controlled evidence

M9 tests frozen predictors in a controlled 1D stochastic family. No predictor is fit to empirical thresholds or sharpness targets.

System-level `eta_c`:

- Model 0/1: MAE `0.6741`, RMSE `0.9053`, R2 `-1.2446`.
- Model 2 (`G_Sigma`): MAE `0.2075`, RMSE `0.2840`, R2 `0.7791`, Spearman `0.8714`.

Matched A-B threshold difference:

- Model 0/1: predicted zero; R2 `-2.2405`.
- Model 2: MAE `0.1476`, RMSE `0.2217`, R2 `0.8485`, Spearman `0.9543`.

System-level sharpness gap:

- Model 1 (projected zero-order noise): R2 `0.9519`.
- Model 2: R2 `0.9943`.

Matched A-B sharpness difference:

- Model 0/1: predicted zero; R2 `-0.1682`.
- Model 2: R2 `0.9835`, Spearman `0.9777`.

Therefore the evidence does **not** support a claim that projected-noise EoS theory fails for the absolute sharpness gap. It supports an incremental role for noise geometry, especially in matched-system differences and stability prediction.

## 4. Higher-order covariance theory

The finite-horizon theory branch contains internal fixed-horizon expansions beyond the additive covariance term.

Current compressed picture:

- order 4: covariance-field curvature `D^2 Sigma` and gradient-noise third cumulant `Gamma` enter the corrected covariance descriptor;
- order 5: additional sectors involve `D Sigma`, `D^3 Sigma`, and the fourth cumulant, with distinct batch-size scalings.

Exact matched-pair constructions show that some of these descriptors are irredundant within the restricted local-jet closure. Generic higher-order weak expansions and cumulant mechanisms have substantial prior art, so publication-level novelty for this hierarchy is not established.

## 5. Important negative results

- Additive zero-mean noise alone does not generically shift the local mean-Jacobian spectrum.
- Pure affine non-Gaussian noise can change the transition operator without changing its eigenvalues; operator separation alone is insufficient.
- A universal temporal-covariance closure for iid SGD is not viable under standard filtration assumptions.
- The earlier finite-horizon covariance-validity certificate is mathematically valid but can be very conservative because it loses stochastic cancellations.
- Higher cumulants alone are not a defensible novelty claim.

## 6. New adjacent branch: finite-sample stability risk

A synthesis branch now asks a statistical question: even if a lifted stability operator is consistently estimable, can the boundary functional `rho(M)=1` be inferred reliably near local alternatives?

Working hypothesis: stochastic stability decisions can become statistically non-regular near the boundary, motivating calibrated `stable / unstable / uncertain` risk statements rather than only point estimates.

This is an active research direction, not a confirmed theorem.

## 7. Current priorities

1. Replicate the `G_Sigma` effect in a genuine finite-sum / minibatch control beyond the continuous-noise 1D family.
2. Test multidimensional noncommuting noise geometry with exact mean-square/Lyapunov baselines.
3. Audit the higher-order covariance-jet results against stochastic-numerics literature before any novelty escalation.
4. Develop the finite-sample stability-boundary branch with an explicit falsification test under local `m^{-1/2}` alternatives.
5. Preserve strict separation between theorem, controlled numerical evidence, exploratory hypotheses, and negative results.
