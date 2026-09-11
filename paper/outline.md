# Paper Outline — Noise Geometry and Finite-Step SGD Stability

## 1. Motivation

Leading local EoS descriptions use curvature and projected gradient-noise magnitude. Ask whether these low-order local descriptors determine finite-step stochastic stability.

## 2. Exact finite-sum counterexample

Construct matched finite-sum SGD systems with equal population Hessian and equal zero-order gradient-noise covariance but different state-dependent noise geometry.

Derive the exact scalar mean-square coefficient

\[
q=(1-\eta\lambda)^2+\eta^2G_\Sigma
\]

and boundary

\[
\eta_c=2\lambda/(\lambda^2+G_\Sigma).
\]

## 3. Descriptor-insufficiency statement

Formulate the result as an existence theorem: `(H, Sigma(0))` and analogous zero-order EoS descriptors are not, in general, sufficient statistics for finite-step mean-square stability.

## 4. Controlled M9 comparison

Use frozen predictors and disjoint EST/EVAL seeds. Report system-level and matched A-B threshold/sharpness metrics.

Emphasize that the projected-noise baseline remains strong for the absolute sharpness gap; the incremental value of `G_Sigma` is strongest in matched differences and threshold prediction.

## 5. Multidimensional extension

Present the exact quadratic-Lyapunov drift and the noise-geometry LMI. Clearly distinguish theorem from conjectured neural relevance.

## 6. Relation to prior work

Position relative to stochastic EoS, discrete finite-step SGD, stochastic modified equations, multiplicative-noise stability, and weak stochastic expansions.

## 7. Limitations

- controlled low-dimensional family;
- no claim that `G_Sigma` is universally sufficient;
- genuine minibatch and neural validation still required;
- higher-order covariance jets have substantial prior-art overlap.

## 8. Falsification experiments

Finite-sum minibatch replication, multidimensional noncommuting control, and held-out neural prediction against GNS/Hessian/projected-noise baselines.
