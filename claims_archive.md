Claim Control

Proven: - SGD minibatch changes conditional transition operator. -
Duffing spectral predictions are validated.

Supported: - Operator perturbation approximately scales with eta/B.

Speculative: - Useful low-dimensional Koopman modes exist for SGD. -
They predict training dynamics better than Hessian/noise baselines.

Forbidden claims: - First spectral theory of SGD. - First discrete SGD
operator. - First projected noise analysis.

Section: Novelty restrictions
Do not claim novelty for: stochastic sharpness suppression by projected gradient noise (covered by Liao et al. 2026), discrete SGD master equations/Fokker-Planck formulations (covered by Ignashin et al. 2026). Novelty candidate remains: predictive low-dimensional closure of SGD transition operators.
Reason:
Снижение риска ложного позиционирования.

Section: Speculative claims
Supported diagnostic evidence: a single global fixed observable-space EDMD closure performs substantially worse than local forward-window fits. Not established: that the true SGD Markov operator is nonstationary. Candidate interpretation: local/state-dependent or measure-dependent projected operator.
Reason: Не допустить завышенного claim по итогам Stage 3C.

Section: Speculative
Post-hoc candidate only: m=5 structured observables show positive short-horizon persistence-normalized skill in the eta=0.05 subset. This is exploratory evidence and cannot be used as confirmation until reproduced on independent seeds and preregistered eta values.
Reason: Контроль post-hoc selection и предотвращение завышенного claim.

Section: Supported / Speculative
Supported secondary evidence: at eta=0.05, B=128, m=5, structured Hessian, gradient-noise and function-space observables show positive one-step persistence-normalized skill on independent seeds. Not supported: independently confirmed two-step closure or slow Koopman modes. Spectral interpretation remains disallowed.
Reason: Не превращать supporting h=1 result в failed h=2 confirmatory claim.

Section: Current claim control
Stage 3F does not provide accepted evidence for structured conditional Koopman closure. Repeated-transition machinery is operational, but D1/D2/D4 scientific results are invalid pending provenance-correct rerun. No stochastic mean correction beyond full-gradient dynamics has yet been resolved.
Reason: Снять ошибочный F2 claim и сохранить строгий scientific status.

Section: Current claim control
Практическая полезность операторного подхода пока не установлена. Допустимо утверждать наличие воспроизводимой нелинейной стохастической поправки условного среднего перехода. Недопустимо утверждать наличие полезных маломерных спектральных мод или преимущество над методами на основе кривизны и ковариации шума до демонстрации независимого предсказательного выигрыша.
Reason: Отделить текущий поддержанный результат от более сильных научных и прикладных заявлений.

Section: Current claim control

Stage 3F-R repaired the provenance failure and reproduced original Stage-3E.2 Phi coordinates to <1e-6 relative error. The D4 stochastic mean correction remains INCONCLUSIVE: at M=128 it is unresolved in 22/24 fixed states. Pooled stochastic-correction skill is positive on the two held-out seeds (~0.16, ~0.14), but this is not accepted evidence because only two test seeds are available and identical Monte-Carlo minibatch sequences were reused across fixed states. No spectral or Koopman-mode claim is allowed. Current gate: independent-pool variance-reduced confirmation.

Reason:

текущий `05_CLAIMS.md` заканчивается состоянием до provenance-correct Stage 3F-R и поэтому тоже требует синхронизации.

Section: Current claim control — after Stage 3I-R HVP audit
Supported strongly: the archived Stage 3I-R nonlinear stochastic conditional-mean correction is predominantly explained by the exact local second-order term C2 = 0.5 E[H_Phi(theta_bar)[delta,delta]] under the tested protocol. Stage 3I-R gives pooled C2 skill ≈0.9272, 6/6 positive seeds at B=128, and approximately 1/B scaling (exponent ≈-0.9857). The dedicated HVP audit returned R-H1 — STRONGLY VALIDATED: independent autograd routes agree, float64 finite differences converge to HVP, all 3072 directions pass the preregistered minimum-error threshold, and archived C2 matches recomputed HVP C2 at scale factor 1.

The previous float32 finite-difference failure is a numerical cancellation artifact and is not evidence against the second-order mechanism. Allowed claim: a reproducible finite-step second-order Hessian/covariance mechanism explains most of the measured local function-space stochastic conditional-mean correction in this archived protocol. Not established: uniform statewise accuracy, universality across architectures/losses/training regimes, a nonzero structured residual beyond second order, low-dimensional Koopman closure, spectral modes, eigenvalue shifts, or practical superiority over Liao-style Hessian/projected-noise or Ignashin-style finite-step local descriptions.

Current gate: determine whether R = C_observed - C2 is reproducibly nonzero after independent-pool variance control, and if so whether it is explained by ordinary third/fourth-order finite-step Taylor terms before any operator/spectral interpretation.
Reason: Upgrade exact-HVP validation while preserving the novelty and mechanism boundaries imposed by Liao et al. 2026 and Ignashin et al. 2026.


## Current claim control — after Stage 3J (2026-09-04)
**SUPPORTED:** Under the tested small-network fixed-state protocol, the reproducible nonlinear stochastic conditional-mean correction is dominated by the validated local second-order Hessian/covariance term C2. Stage 3J finds no independently resolved residual beyond C2 at B=128: pooled TARGET/AUDIT residual skill ≈0.1436 with seed-bootstrap 95% CI ≈[-0.3027,0.4119], only 2/6 positive seed skills, and residual energy roughly 0.15%–0.40% of C2 energy across trajectory fractions.

**INCONCLUSIVE:** The exact mathematical remainder beyond C2 may be nonzero; Stage 3J only shows that it is not resolved above current independent-pool uncertainty. Third/fourth-order C3/C4 explanations are also INCONCLUSIVE because per-scale convergence curves were not retained and therefore derivative-order validation cannot be reconstructed.

**ALREADY KNOWN / NOT A NOVELTY CLAIM:** Generic finite-step stochastic corrections, discrete-SGD operator formulations, projected gradient-noise/Hessian effects, and weak stochastic modified equation expansions are established prior art. The project must not claim novelty merely for the existence of C2 or eta^2/B-type corrections.

**PRELIMINARY / UNTESTED:** A practical zero-fit predictor based on locally measured gradient covariance and exact HVP contractions may predict finite-B, finite-eta conditional transitions on unseen states/conditions. This is the Stage 3K hypothesis and is not yet supported.

**NOT SUPPORTED:** low-dimensional Koopman closure, spectral modes/eigenvalue shifts for SGD, a structured residual beyond C2, universality across architectures/losses, or practical superiority over existing Hessian/noise approaches.

Current gate: Stage 3K must freeze predictions before TARGET measurements on new scientific seeds/states, test them over a preregistered eta×B grid, quantify seed-level uncertainty, compare against simpler baselines, and identify the boundary where C2 ceases to be quantitatively accurate.


## Current claim control — after Stage 3K repaired analysis (2026-09-04)
**SUPPORTED STRONGLY:** On fresh preregistered network seeds and fixed states, the local second-order Hessian/gradient-covariance predictor C2, computed and frozen before TARGET/AUDIT sampling, quantitatively predicts the function-space stochastic conditional-mean correction over the tested eta×B grid. Corrected core pooled skill ≈0.9013 with seed-bootstrap 95% CI ≈[0.6931,0.9491]; full-grid skill ≈0.8791. All 25/25 preregistered conditions have positive pooled skill and positive bootstrap lower bounds. No validity boundary is resolved inside eta∈[0.0125,0.1], B∈[32,512].

**SUPPORTED:** The scalar/isotropic-noise approximation is insufficient in this protocol (core skill ≈0.0201), supporting the importance of covariance orientation relative to curvature. A corrected single-reference C2 extrapolated by eta^2/B performs essentially as well as recomputing eta-dependent curvature: core/full skills ≈0.9023/0.8807 versus ≈0.9013/0.8791, with FULL−FROZEN core CI including zero.

**IMPORTANT LIMITATION:** Accuracy is heterogeneous across network realizations. Equal-seed core mean/median ≈0.665/0.854 and seeds 34–35 contribute ≈92.84% of core target energy. The ≈0.90 pooled skill is not a claim of ≈0.90 accuracy for every seed.

**NOT NOVEL BY ITSELF:** eta^2/B finite-step corrections, discrete SGD operators, gradient-noise covariance, curvature/noise alignment, projected top-Hessian noise, gradient noise scale, or adaptive batch-size ideas.

**NOT YET SUPPORTED:** that the diagnostic chooses a useful/optimal batch size; that it predicts generalization, optimization speed, long-horizon behavior, EoS/cross-entropy regimes, large architectures, or cross-task universality; that it outperforms McCandlish gradient-noise-scale or Liao-style projected-noise/Hessian diagnostics on a downstream outcome; any Koopman/spectral claim.

Current gate: Stage 3L must test downstream practical value. A single reference C2 measurement and all competing baseline diagnostics must be frozen before independent multi-step trajectory outcomes are generated. The key question is whether C2 predicts a preregistered short-horizon material stochasticity threshold/batch regime better than simpler local statistics.

## Current claim control — after Stage 3L / Stage 3L-R (2026-09-04)
**SUPPORTED STRONGLY FROM STAGE 3K:** The local one-step C2 mechanism can make frozen zero-fit predictions of finite-eta/finite-B conditional-mean corrections in the tested small-network regime.

**NOT SUPPORTED AS A PRACTICAL DOWNSTREAM CLAIM:** Stage 3L does not establish that a one-shot C2 diagnostic predicts a useful H=10 materiality/batch threshold or outperforms GNS/isotropic/projected-noise baselines. After debiasing, no H=10 condition passes the repaired outcome-resolution gate.

**SUPPORTED DIAGNOSTIC LESSON:** The original norm-based H=10 materiality was substantially contaminated by finite-Monte-Carlo positive norm bias. The analysis-only repair found median original materiality ≈6.28 times the cross-fitted estimate, positive cross-energy on only ≈50.46% of H=10 conditions, and ≈50.93% sign agreement between independent pool-debiased energies.

**INCONCLUSIVE:** Whether naive `H*C2` accumulation is quantitatively wrong. The repaired mean-shift target is too poorly resolved to test that hypothesis.

**PRELIMINARY / NEW HYPOTHESIS:** Finite-horizon stochastic covariance in function space may be a better-resolved target. Stage M1 will test zero-fit prediction of that covariance from local gradient-noise covariance propagated through tangent Hessian dynamics along the deterministic path.

**NOT NOVEL BY ITSELF:** finite-time covariance recursions, Lyapunov-type covariance propagation, quadratic SGD fluctuation formulas, Hessian-basis variance dynamics, or generic memory kernels.

**FORBIDDEN UNTIL LATER EVIDENCE:** random-reshuffling memory, non-Markovian SGD, temporal covariance `K_st`, optimizer memory, practical schedule optimization, large-model universality, or superiority to whole Ignashin/Liao/DMFT theories.


## Current claim control — after Stage M1 (2026-09-05)
**SUPPORTED STRONGLY:** In the tested small-CNN i.i.d.-minibatch regime, finite-horizon function-space covariance of nonlinear SGD trajectories is quantitatively predictable zero-fit from premeasured anisotropic gradient noise propagated through matrix-free tangent/HVP dynamics along the matched deterministic path. At H=10, mean Frobenius skill ≈0.9267 with seed-bootstrap 95% CI ≈[0.9155,0.9381], matrix cosine ≈0.9792, trace relative error ≈0.114, and top-eigenspace overlap ≈0.978. TARGET/AUDIT covariance independently replicates at H=1,5,10.

**SUPPORTED:** Temporal propagation is essential beyond one step: at H=10 the full predictor beats the no-propagation baseline by ≈0.650 Frobenius skill with CI far above zero. Anisotropic gradient-noise structure is also essential for matrix prediction: full minus isotropic ≈0.915 skill. 

**SUPPORTED BUT SMALL EFFECT:** Updating geometry along the deterministic path improves over frozen-geometry propagation only modestly at H=10: Δskill ≈0.014 with 95% CI ≈[0.0019,0.0251]. Do not describe moving geometry as the dominant source of predictive power.

**IMPORTANT BASELINE LIMITATION:** A scalar parameter-noise/GNS-style score has Spearman ≈0.981 with TARGET covariance trace at H=10. Therefore M1 does not establish unique value for predicting total variance magnitude. Its stronger contribution is matrix-level covariance geometry/eigenspace prediction beyond isotropic/scalar summaries.

**NOT NOVEL BY ITSELF:** covariance recursion, tangent linearization, Hessian propagation, 1/B minibatch covariance scaling, random-reshuffling convergence advantages, or the existence of SGD memory.

**NOT YET SUPPORTED:** explicit temporal-memory/cross-time covariance terms under reshuffling, non-Markovian SGD claims, optimizer memory, random-reshuffling predictive theory, universality across architectures/data/losses, large-model validity, generalization gains, or optimal batch-size guidance.

Current gate: Stage M2 must change only the sampling temporal structure and test whether explicit off-diagonal `K_st` terms predict the deviation from the validated M1 i.i.d. covariance baseline.
