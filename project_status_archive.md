SGD Spectral Research Project - Current Status

Main question: Does SGD contain low-dimensional stochastic Koopman modes
that predict training dynamics beyond Hessian and gradient-noise
methods?

Completed: - Duffing spectral validation. - Spectral time validation
against correlations and relaxation. - SGD minibatch noise
measurements. - Conditional fixed-design operator estimation.

Current stage: Koopman closure audit.

Open question: Does there exist an observable space V where P_B(V)
approximately equals V and the spectrum predicts real SGD dynamics?
dit update: Liao et al. (2026) show stochastic self-stabilization through projected gradient noise variance and sharpness dynamics. Ignashin et al. (2026) reinforce the need for discrete SGD transition operators instead of pure Langevin approximations. Project novelty must avoid claims about noise projection, discrete operators, or generic spectra. The remaining target is predictive closure of low-dimensional stochastic Koopman observable spaces.
Reason:
Обновление проекта после анализа новых работ и уточнение научного зазора.
Koopman closure benchmark reached the scientific gate and failed to satisfy closure acceptance. Prediction testing is suspended. Current priority is a closure-failure audit distinguishing genuine non-closure, estimation/conditioning error, SGD nonstationarity, and irreducible stochastic variance.
Reason:
Update the project from closure search to diagnosis of the failed closure gate.

Closure-failure audit indicates that local forward-window EDMD substantially outperforms a global fixed EDMD projection. However, this should not yet be interpreted as intrinsic time-dependence of the SGD Markov kernel. The working hypothesis is modified toward state-local or sampling-measure-dependent finite-dimensional projections of an underlying SGD transition operator.
Reason: Разделить истинную динамику SGD и зависимость конечномерной EDMD/Galerkin аппроксимации от области state space и sampling measure.
Global hyperparameter-independent Koopman closure is not supported. Current diagnostic question is whether a reproducible short-horizon low-dimensional predictive regime exists at larger finite learning rate, rather than whether one fixed observable space closes SGD across all training conditions.
Reason: Уточнить гипотезу после persistence-normalized benchmark.

Aggregate global fixed-dictionary closure remains unsupported, but Stage 3E.1 identified a specific high-eta, low-dimensional, short-horizon candidate regime. Current priority is independent preregistered confirmation on unused seeds, with no hyperparameter search.
Reason:

Shift project from exploratory subgroup discovery to confirmatory falsification.
Independent confirmation rules out promotion of the h=2 candidate to a Koopman-closure claim. Evidence instead points toward short-horizon/conditional structured dynamics. Current priority is repeated fixed-state minibatch transition estimation to separate conditional-mean signal from irreducible stochastic variance.
Reason: Перевести проект от trajectory EDMD к conditional operator estimation.

Provenance-correct paired fixed-state estimation shows that one-step conditional means are largely deterministic full-gradient drift plus an unresolved nonlinear stochastic correction. Current priority is variance-reduced independent-pool estimation of the nonlinear function-space correction before deciding whether conditional stochastic operator structure exists.
Reason: Сместить фокус на непосредственное измерение stochastic correction, а не trajectory EDMD.

Current conceptual objective
Текущий проект больше не проверяет наличие спектра у SGD как такового. Центральная задача — выяснить, существует ли воспроизводимая маломерная структура условного оператора перехода, которая даёт предсказательную информацию сверх кривизны функции потерь, масштаба и ковариации градиентного шума. Последний этап отделяет обычную нелинейную поправку второго порядка от возможной дополнительной структурированной динамики.
Reason: Зафиксировать научную цель после отрицательных результатов по глобальному замыканию и после обнаружения воспроизводимой стохастической поправки.

Current priority
Stage 3H resolves the previous D4 correction ambiguity in favor of a strong local second-order mechanism. Current priority is Stage 3I: exact Hessian-vector covariance-contraction validation and fixed-state 1/B scaling audit before any return to spectral interpretation. If successful, the next scientific gate is whether the corrected conditional operator improves out-of-sample low-dimensional closure beyond Hessian, projected-noise, noise-scale, and random baselines.
Перевести проект от обнаружения correction к точной discrete-operator механике и сохранить predictive objective.
Current priority — after Stage 3I-R HVP audit
Stage 3I-R independently reproduced the finite-step nonlinear function-space conditional-mean correction on a new dataset subset, new trajectories, new F_new, six network seeds, and independent stochastic pools. The exact second-order predictor C2 achieves pooled skill ≈0.9272 (95% CI ≈[0.8445,0.9556]), no-calibration slope ≈0.8291, 6/6 positive seeds at B=128, and batch scaling exponent ≈-0.9857 with CI containing -1. The subsequent HVP falsification audit returned R-H1 — STRONGLY VALIDATED: two independent exact-autograd HVP routes agree to ~1e-16 in float64, all 3072/3072 archived directions admit finite-difference error <0.25, and archived C2 matches recomputed HVP C2 with median relative error ≈2.1e-7 and cosine ≈1 at scale factor 1. The earlier failed HVP sanity check is attributable to float32 cancellation in function-value second differences, not to a mathematical or scaling error in C2.

The exact local second-order Hessian/covariance mechanism is therefore accepted for the archived Stage 3I-R protocol. No EDMD, Koopman, generator, eigenvalue, spectral-shift, universality, or global-SGD claim follows. The next scientific gate is to resolve the conditional residual after subtracting the validated second-order term and determine whether it is (i) Monte-Carlo noise, (ii) ordinary higher-order finite-step Taylor physics, or (iii) a reproducible residual structure with predictive content beyond local Hessian/noise mechanisms. No return to spectral interpretation is allowed before this residual gate is passed.
Reason: Stage 3I-R and the dedicated HVP audit close the numerical-mechanism gate and move the project from validating C2 to falsifying any claimed structure beyond C2.


## Current priority — after Stage 3J repaired analysis (2026-09-04)
Stage 3J (`stage3j_residual_beyond_c2_20260903T181151Z`, analysis-only repaired) completed the full scientific grid before the final analysis repair: 6 network seeds × 4 trajectory fractions × 5 batch sizes = 120 saved scientific NPZ blocks. The repair did not rerun SGD, gradients, HVPs, or stochastic pools; it reused the completed blocks, fixed only the analysis aggregation bug, and retained PASS provenance to the Stage 3I-R source objects.

Final Stage 3J verdict: **J1 — NO RESOLVED RESIDUAL**. At the preregistered primary batch B=128 across 24 fixed states, pooled TARGET/AUDIT cross-replicate skill is ≈0.1436, pooled cosine ≈0.1474, seed-bootstrap 95% CI for skill ≈[-0.3027, 0.4119], only 2/6 network seeds have positive skill, and the fraction of states with positive cosine is 0.50. The measured residual energy is small relative to C2: across trajectory fractions, residual/C2 energy is approximately 0.15%–0.40%. Therefore the current data do not support a reproducible conditional-mean structure beyond the validated local second-order term at this resolution.

Stage 3J does **not** prove that the exact mathematical remainder is zero. It only shows that a residual beyond C2 is not independently resolved by the current experiment. Higher-order C3/C4 claims are also not authorized because the interrupted run retained only median T3/T4 summaries across scales; the per-scale convergence curves required to validate third/fourth-order derivative interpretation were not preserved.

Strategic consequence: stop residual escalation and do not return to EDMD/Koopman/spectral interpretation. The active project objective becomes **Stage 3K: zero-fit out-of-sample finite-step prediction and boundary-of-validity testing**. The next experiment must use new scientific seeds/states and freeze predictions from locally measured gradient covariance + exact Hessian-vector contractions before measuring TARGET transitions at unseen (eta,B) conditions. The purpose is to test whether the validated C2 mechanism can quantitatively predict finite-B, finite-eta conditional transitions and to map where it fails. Practical usefulness and publication value now depend on predictive performance and validity boundaries, not on the existence of the already-known generic finite-step correction mechanism.

Reason: Stage 3J closes the residual gate negatively at current resolution and shifts the project from searching for extra local operator structure to exploiting and stress-testing the validated finite-step C2 mechanism as a zero-fit predictor.


## Current priority — after Stage 3K repaired analysis (2026-09-04)
Stage 3K (`stage3k_zero_fit_finite_step_prediction_20260904T004119Z`) was completed as a preregistered zero-fit predictive experiment on fresh network seeds 31–36, new fixed states, a 5×5 eta×B grid, and predictions frozen+hashed before TARGET/AUDIT generation. The original automated K5 diagnosis was invalidated by an analysis-only repair (`stage3k_zero_fit_finite_step_prediction_20260904T004119Z_analysis_repaired_20260904T073851Z`). Scientific generation was not recomputed and prediction-freeze integrity was verified.

Final repaired verdict: **K1-R — STRONG ZERO-FIT PREDICTION; BOUNDARY NOT REACHED.** Corrected core pooled C2 skill is ≈0.90129 with seed-bootstrap 95% CI ≈[0.69308,0.94905]; full-grid pooled skill ≈0.87908. All 25/25 preregistered eta×B conditions have positive pooled skill, bootstrap lower CI >0, and pass the strong-valid criterion. Therefore no reproducible validity boundary is observed inside eta∈[0.0125,0.1], B∈[32,512].

Two postprocessing failures were confirmed: (i) condition-wise skill had been averaged across unstable statewise normalized ratios instead of computed from pooled SSE; (ii) the frozen-reference baseline had an extra B_ref factor, inflating it by 128. After correction, the cheap single-reference predictor
`C2_frozen(eta,B)=C2_ref*(eta/eta_ref)^2*(B_ref/B)`
performs essentially identically to the full eta-dependent C2: core/full skills ≈0.90227/0.88067 versus ≈0.90129/0.87908. FULL−FROZEN core skill difference ≈−0.00098 with 95% CI ≈[−0.00435,0.00196], so recomputing curvature at every eta is not measurably better in the tested range.

Important limitation: prediction is heterogeneous across network seeds. Equal-seed mean/median core skill ≈0.665/0.854, while seeds 34–35 contribute ≈92.84% of core target energy. The pooled ≈0.90 skill is therefore a valid energy-weighted statement about the measured stochastic signal, not a claim of ≈0.90 accuracy for every network realization.

Current scientific objective: move from one-step predictive validation to **practical falsification**. The next gate is Stage 3L: test whether a single local reference C2 measurement can predict when minibatch stochasticity becomes materially important for short-horizon function-space training dynamics, and whether it does so better than scalar eta/B, gradient-noise-scale, isotropic-noise, sharpness, and projected-noise baselines. Predictions and any materiality threshold must be preregistered before trajectory outcomes are generated. No adaptive-batch/generalization/large-model claim is allowed before this downstream test succeeds.

Reason: Stage 3K passes the zero-fit prediction gate and shows that the tested eta×B grid lies inside the C2-valid regime. The project should now test downstream practical value rather than repeat one-step C2 validation or return to Koopman/EDMD.

## Current priority — after Stage 3L / Stage 3L-R (2026-09-04)
Stage 3L (`stage3l_one_shot_c2_short_horizon_materiality_20260904T080455Z`) tested whether one frozen local C2 reference measurement could predict a materially important H=10 function-space stochastic mean shift and a useful batch threshold on fresh network seeds 41–46. Prediction freeze and fresh-data provenance passed. The original run returned **L4 — OUTCOME UNRESOLVED**.

A dedicated analysis-only repair (`stage3l_analysis_repaired_debiased_20260904T122818Z`) reused the saved TARGET/AUDIT trajectories without new SGD, HVP, gradients, or mechanism samples. It replaced the positively biased finite-Monte-Carlo norm of the sample mean by the independent cross-fitted signal-energy estimator `S2_cross = Delta_TARGET^T Delta_AUDIT` and an independent per-pool covariance debiasing check.

Final repaired verdict: **LR4 — REPAIR STILL INCONCLUSIVE**, with a scientifically important negative practical result. At H=10, only ≈0.50463 of conditions have positive cross-fitted signal energy, the two pool-debiased estimates agree in sign only ≈0.50926 of the time, and **0 conditions** pass the repaired replication/SNR gate. The median original norm-based materiality is ≈6.28 times the cross-fitted estimate. Therefore the H=10 conditional-mean shift required by the proposed practical batch diagnostic is not resolved at the current trajectory budget. The data do not support a claim that naive `H*C2` accumulation fails; after debiasing there is insufficient resolved mean-shift signal to test that claim.

Strategic consequence: close the immediate attempt to turn C2 into a short-horizon mean-shift batch selector. Do not spend the next stage merely multiplying trajectory count to rescue this endpoint. The new active objective is **Stage M1 — zero-fit finite-horizon covariance propagation under i.i.d. minibatching**. The target becomes the stochastic trajectory covariance in neural-network function space, which is substantially easier to resolve than a tiny second-order mean shift. The primary hypothesis is that locally measured gradient-noise covariance propagated through the tangent linear dynamics along the deterministic training path can predict the held-out covariance cloud at H=1,5,10 before stochastic rollout. Random reshuffling / temporal noise correlation is a later extension and must not be claimed in M1.
Reason: Stage 3L-R shows that the practical mean-shift endpoint is Monte-Carlo limited and does not support downstream superiority; finite-horizon covariance is the next better-resolved dynamical object and creates a clean i.i.d. baseline before any correlated-sampling theory.


## Current priority — after Stage M1 (2026-09-05)
Stage M1 (`stage_m1_finite_horizon_covariance_iid_20260904T164751Z`) completed on the fresh small-CNN/CIFAR-10 protocol with predictions frozen before nonlinear TARGET/AUDIT rollouts. Final diagnosis: **M1 — FINITE-HORIZON COVARIANCE PROPAGATION SUPPORTED.** At H=10, mean Frobenius skill ≈0.92668 with seed-bootstrap 95% CI ≈[0.91548,0.93812], matrix cosine ≈0.97920, trace relative error ≈0.1143, top-eigenvalue relative error ≈0.1663, and top-1 eigenspace overlap ≈0.9776. TARGET/AUDIT covariance replication is strong at H=1,5,10 and all six seeds have high positive H=10 skill.

Mechanism decomposition: full propagation strongly beats no-propagation (Δskill ≈+0.650 at H=10) and isotropic-noise propagation (Δskill ≈+0.915), while the gain over frozen geometry is small but positive (≈+0.014). A scalar GNS-like score already ranks covariance trace extremely well (Spearman ≈0.981), so the distinctive supported result is prediction of **matrix covariance geometry/eigenspaces**, not unique prediction of total variance magnitude. An earlier post-scientific plotting crash (`KeyError('target_trace')`) remains archived; final scientific acceptance relies on already-persisted frozen predictions/raw arrays and successful resume-safe analysis.

Strategic consequence: the i.i.d. finite-horizon baseline is established. The new active objective is **Stage M2 — causal test of temporal minibatch correlations under random reshuffling**. M2 must isolate off-diagonal cross-time covariance from one-step finite-population effects by comparing random reshuffling against an independently resampled without-replacement control with the same one-step marginal batch covariance. Predictions must be frozen before all new RR/control trajectory outcomes.
Reason: M1 shows that anisotropic covariance propagation is a quantitatively accurate zero-fit baseline; this now permits a clean test of whether realistic data-order correlations add predictive structure beyond diagonal-in-time noise.
