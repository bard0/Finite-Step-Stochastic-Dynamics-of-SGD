# Final Research Summary — Project Freeze v1.0

**Project:** Finite-Step Stochastic Dynamics of SGD  
**Freeze date:** 2026-09-30  
**Status:** v1.0 complete. Publication-oriented extensions are treated as a separate possible v2.

## 1. Research question

The project began from a simple question: can stochastic gradient descent be understood through the spectrum of an effective stochastic evolution operator, and can this viewpoint predict how minibatch noise changes stability and relaxation?

The finite-step formulation uses

\[
(P_\eta f)(\theta)=\mathbb E\,f(\theta-\eta g_B(\theta)).
\]

The project gradually moved away from treating SGD as “gradient descent plus a scalar noise amplitude” and toward a sharper question:

> **Which stochastic information is sufficient to predict finite-step SGD dynamics?**

The question changed because several early hypotheses failed while a smaller set of effects survived controlled tests.

## 2. Research trajectory

### Stage A — spectral perturbation and controlled stochastic models

The initial branch treated stochasticity as a perturbation of local deterministic dynamics and studied shifts of spectral modes. Controlled Duffing experiments were used as a physically interpretable testbed because slow modes, metastability, relaxation times, and Kramers-type behavior can be checked independently.

In the controlled Duffing test, predicted and measured spectral shifts agreed very closely: mean absolute error about \(1.5\times10^{-7}\), median relative error about \(2.5\times10^{-3}\), and Spearman correlation about \(0.999\). This showed that the perturbative calculation can be numerically accurate when its assumptions are satisfied.

A complementary additive-noise unit test showed essentially no physical mean spectral shift. This ruled out a simple explanation: **noise amplitude by itself is not the mechanism.**

### Stage B — state-dependent stochastic geometry

The next branch asked whether the geometry of gradient noise matters. The project found controlled examples in which state-dependent covariance changes finite-step stability even when lower-order local descriptors are matched.

For the exactly solvable scalar multiplicative-noise model,

\[
q=(1-\eta\lambda)^2+\eta^2G_\Sigma,
\qquad
\eta_c=\frac{2\lambda}{\lambda^2+G_\Sigma}.
\]

This provides an analytical descriptor-insufficiency construction: matching the population Hessian and zero-order gradient-noise covariance does not in general determine the exact finite-step second-moment stability boundary.

This is an existence result. The project does **not** claim that multiplicative noise, state-dependent diffusion, or mean-square stability theory are themselves new.

### Stage C — controlled M9 prediction benchmark

M9 tested whether the noise-geometry descriptor has observable predictive value in a controlled family.

Key results:

| Target | simpler baseline | noise-geometry model |
|---|---:|---:|
| system-level \(\eta_c\), \(R^2\) | -1.2446 | **0.7791** |
| matched A-B \(\Delta\eta_c\), \(R^2\) | -2.2405 | **0.8485** |
| absolute sharpness gap, \(R^2\) | 0.9519 | **0.9943** |
| matched A-B \(\Delta S\), \(R^2\) | -0.1682 | **0.9835** |

The projected-noise baseline already explains most of the **absolute** sharpness gap. The strongest evidence for the additional descriptor is therefore in matched-system separation and stability-threshold prediction, not in a claim that leading projected-noise EoS theory is broadly wrong.

### Stage D — temporal structure hypothesis and repair

A major intermediate hypothesis was that temporal covariance of centered SGD noise could provide a universal missing descriptor.

This did not survive the filtration audit. For conditionally unbiased independently resampled minibatches, centered innovations are martingale differences, so generic nonzero cross-time centered covariance cannot be treated as a universal iid-SGD memory mechanism.

Further repaired neural experiments also showed that a simple linear temporal-covariance closure did not outperform a marginal covariance baseline in the tested regime.

I dropped this as a general mechanism. The useful outcome was methodological: later experiments used stricter causal designs and separated temporal-ordering effects from any claim of a universal covariance-memory theory.

### Stage E — higher-order neural transfer and falsification

The neural branch then tested a concrete higher-order geometric descriptor,

\[
\chi_{mix}=D^4L[u,u,v,v],
\]

against a strong lower-order baseline in a preregistered held-out design.

Across 30 checkpoints from 16 seed groups:

- MAE: \(2.0926\to1.9942\);
- pooled MAE gain: \(4.70\%\);
- \(\Delta R^2=0.00325\);
- seed-group bootstrap CI for MAE gain: \([-0.0619,0.1511]\);
- residual Spearman: \(0.3277\), with CI crossing zero;
- sign agreement: \(0.6333\);
- paired permutation \(p=0.0428\).

The frozen regime-robust success gates were not jointly satisfied. The confirmatory verdict is therefore:

**FAIL_NO_PRIMARY_NEURAL_INCREMENTAL_VALUE.**

The apparent gain was heterogeneous across learning-rate regimes and is retained only as exploratory evidence. The practical lesson was simple: **being able to measure a complicated descriptor does not mean it will improve prediction.**

## 3. Final theoretical viewpoint

By the end, the project was best described as a finite-step **spectral closure / information sufficiency** problem.

The question is no longer whether one can write another term in a stochastic Taylor expansion. Such higher-order terms overlap strongly with stochastic modified equations, weak expansions, cumulant expansions, B-series, and multiplicative-noise theory.

The sharper question is:

> Given a target finite-step observable or spectrum, what compressed stochastic information is sufficient to determine it to a stated order and horizon?

The late proof work produced several local matched-information constructions, but also exposed limits of the compact closures I was trying to derive. In particular, compact quotients derived for frozen stochastic laws did **not** survive unrestricted moving stochastic laws without additional time-ordered information. So I did not promote the frozen-law calculation to a universal low-dimensional closure.

These advanced local constructions are archived as a possible v2 research direction, not promoted as a final v1 headline theorem.

## 4. Final claim ledger

### Confirmed analytical / methodological

1. **Additive zero-mean noise alone is not a generic source of physical mean spectral shift in the controlled setting.**
2. **Low-order local descriptors can be insufficient for exact finite-step mean-square stability:** an explicit scalar finite-sum construction changes the stability boundary through state-dependent noise geometry while matching the lower-order reference descriptors.
3. **A universal centered temporal-covariance memory mechanism is not valid for ordinary iid/with-replacement SGD under standard conditional-unbiasedness assumptions.**

### Controlled numerical support

4. **Controlled Duffing perturbation theory can be extremely accurate when its assumptions are enforced.**
5. **M9 supports incremental predictive value of state-dependent noise geometry**, especially for matched-system stability-threshold and sharpness-separation tasks.

### Confirmatory negative result

6. **The preregistered regime-robust neural incremental-value claim for \(\chi_{mix}\) failed** under the tested G8.10-B4 design.

### Exploratory / not promoted

7. Eta-dependent higher-order neural effects, long-horizon EoS coupling quotients, and moving-reference spectral-closure theorems remain open research directions rather than v1 claims.

## 5. What the project does not claim

The frozen v1 project does **not** claim:

- a universal spectral law for neural-network SGD;
- a universal critical batch-size formula;
- a new general theory of state-dependent noise;
- that Koopman theory is the central novelty;
- that higher cumulants are themselves a new mechanism;
- that the failed \(\chi_{mix}\) neural test can be rescued by post-hoc regime selection;
- that the latest local matched-information proofs establish a general moving-PGD or long-horizon EoS theorem;
- a new optimizer or demonstrated generalization improvement.

## 6. Relation to nearby 2026 work

The final framing sits between two complementary lines.

- **Liao et al. (2026):** leading EoS/sharpness dynamics compressed into curvature, nonlinear restoring geometry, and projected noise variance.
- **Ignashin et al. (2026):** finite-step SGD retains information that Brownian/Langevin closures can lose.

The v1 contribution is a **descriptor-sufficiency study**: controlled examples, an analytical counterexample, predictive benchmarks, and negative tests that show where simpler descriptions stop being adequate.

## 7. Why stop here?

At this point the main claims are clear, the important negative results are documented, and the remaining questions require genuinely new theory or new data.

A moving-reference or long-horizon closure theorem, a theorem-level priority check, or another prospective neural experiment would be a separate project rather than cleanup needed to finish v1.

## 8. Final project statement

**Finite-step SGD dynamics cannot, in general, be reduced to a single scalar noise amplitude or an unqualified low-order stochastic closure. Controlled models show that state-dependent stochastic geometry can change stability and matched-system dynamics, while the neural tests show that adding higher-order descriptors does not automatically improve prediction. The main outcome of v1 is a clearer boundary between stochastic descriptions that work in the tested settings and those that do not.**
