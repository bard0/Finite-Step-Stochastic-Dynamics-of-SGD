# Higher-Order Finite-Horizon Covariance Jets

## Status

Internal theory; mathematically developed but publication novelty remains uncertain because the generic ingredients overlap with classical stochastic numerical analysis.

## Fixed-horizon expansion structure

For iid with-replacement minibatch SGD around a moving deterministic trajectory, the covariance expansion has the schematic structure

\[
\operatorname{Cov}(e_H)
=
\frac{\eta^2}{B}\widehat Q_H
+
\frac{\eta^4}{B^2}C_{4,H}
+
\frac{\eta^5}{B^2}C_{5,2,H}
+
\frac{\eta^5}{B^3}C_{5,3,H}
+
O_H(\eta^6/B^2).
\]

After algebraic compression:

- order 4 requires covariance-field curvature `D^2 Sigma` and the third gradient-noise cumulant `Gamma`, together with deterministic trajectory geometry;
- order 5 adds sectors involving `D Sigma`, `D^3 Sigma`, and the fourth cumulant, with different powers of `1/B`.

## Important correction

Several initially proposed mixed forcing tensors were redundant. They collapse into derivatives of the state-dependent covariance field. The compact descriptor set is therefore smaller than the raw Taylor expansion suggests.

## Matched-pair / necessity evidence

Explicit local finite-sum pairs show that selected order-4 descriptors can be irredundant within the restricted jet closure: matching lower descriptors while changing one higher descriptor can change finite-horizon covariance at the corresponding order.

This is a compression/minimality statement, not full Markov-kernel identifiability. The complete pointwise stochastic-gradient law determines the iid transition kernel.

## Novelty boundary

Do not market these tensors as new stochastic objects. Higher moments, cumulants, state-dependent diffusion coefficients, weak expansions, stochastic B-series, and Talay–Tubaro corrections are established. The open contribution is whether a compact SGD-specific descriptor quotient yields a useful and sharp prediction/validity theorem.
