Experiment Log

Experiment 001: Duffing spectral validation. SUCCESS.

Experiment 002: SGD noise scaling. Found approximately 1/B scaling.
Universal eta/(BN) rejected.

Experiment 003: Independent EDMD subtraction. FAILED due to error
amplification.

Experiment 004: Conditional operator estimation. SUCCESS.
Batch-dependent operator perturbation detected.

Experiment 007 — Full Koopman closure benchmark. Full EDMD closure benchmark completed. Stage-3 closure gate did not pass, therefore Stage-4 predictive benchmark was correctly skipped. Current fixed Hessian, gradient-noise, random-projection, and function-space observable classes do not yet provide accepted evidence of predictive low-dimensional closure. Random low-dimensional projections appear competitive in the reported H=10 closure diagnostic, weakening interpretation of structured dictionaries. Result status: INCONCLUSIVE with negative evidence against the current fixed-dictionary formulation; closure failure decomposition is required before modifying or rejecting the broader Koopman hypothesis.
Reason:
Record the first substantive negative closure result while separating failure of tested observable classes from failure of Koopman structure in general.

Experiment 008 — Stage 3D projection-drift audit. Stage 3D completed with formal diagnosis D5 INCONCLUSIVE. Cross-window EDMD transfer error increases monotonically with temporal/state separation, supporting state-locality of finite-dimensional approximations as a candidate explanation. However, aggregate local/global improvement is modest and window-dependent, operator drift correlates only weakly with Gram/cross-moment drift, and structured dictionaries do not consistently outperform random projections in absolute closure. Measure-dependent EDMD projection is therefore not yet established.
Reason: Separate robust empirical observations from the stronger automated interpretation.
Stage 3E
Persistence-normalized audit rejects aggregate global fixed-dictionary closure: no tested structured dictionary provides reproducible out-of-sample predictive skill over persistence, and multi-step skill is broadly negative. However, post-hoc stratification reveals a possible short-horizon regime at eta=0.05 and m=5, where Hessian, gradient-noise and function-space dictionaries show positive mean one-step skill while matched random projections remain negative. This regime requires exploratory stratified audit followed by independent confirmation before any claim.
Reason: Не потерять потенциально содержательный finite-step regime из-за агрегации по learning rate.
Stage 3E.1 — regime-stratified audit  
Exploratory regime-stratified audit returned R1: candidate high-learning-rate short-horizon structured signal. The strongest preregistered candidate is eta=0.05, B=128, Hessian dictionary m=5, horizon h=2. Mean test skill is approximately 0.262 with all three exploratory seeds positive; matched random projections are strongly negative. Similar but weaker candidate regimes appear for Hessian B=512, gradient-noise dictionaries, and function-space B=512. Evidence is post-hoc and not confirmatory.
Reason:  
Preserve the finite-step regime signal while explicitly separating exploratory evidence from independent validation.
Stage 3E.2 — independent confirmation

Pre-registered eta=0.05, B=128, Hessian m=5, h=2 candidate was not independently confirmed. Mean Skill_2=0.121, median=0.233, 5/6 seeds positive, exact one-sided p=0.109, bootstrap 95% CI=[-0.157,0.336]. Hessian nevertheless beats matched random projections at h=2 (mean delta skill≈0.923, CI>0). Pre-specified supporting h=1 analyses show reproducible positive structured skill: Hessian 5/6 positive, gradient-noise 6/6 positive, function-space 5/6 positive. Status: multi-step candidate not confirmed; one-step structured signal supported as secondary evidence.
Reason: Сохранить distinction между failed primary endpoint и воспроизводимым supporting one-step signal.

Stage 3F audit
Stage 3F automated F2 diagnosis invalidated by post-run archive audit. The run used a synthetic provenance_backfill and reports bases_seed_6.npz as D1/D2/D3/D4 basis provenance for all seeds. Direct comparison with original Stage 3E.2 artifacts shows that Stage-3F observables do not reproduce original D1 Hessian, D2 gradient-noise, or D4 function-space Phi coordinates; only D3 random matches. Structured conditional conclusions are therefore not accepted. A second issue was identified in structured-vs-random aggregation: averaging per-state skill ratios is unstable for near-zero conditional increments.
Reason: Зафиксировать invalidation результата до того, как F2 попадёт в claims

Stage 3F-R
Stage 3F-R successfully repaired provenance: original Stage-3E.2 Phi coordinates are reproduced to <1e-6 relative error and all D1/D2/D3 linear expectation null controls pass. D4 stochastic mean correction is not resolved at current M=128 in 22/24 fixed states. Total D4 conditional mean is not reproducibly predicted beyond persistence and is strongly dominated by the deterministic full-gradient baseline. However, post-run audit found that pooled stochastic-correction prediction skill is positive on both held-out seeds (~0.16 and ~0.14), while the automated report averaged unstable per-state skill ratios. This signal remains inconclusive because only two test seeds exist and identical minibatch Monte-Carlo sequences were reused across fixed states within a seed.
Reason: Сохранить валидные результаты Stage 3F-R и не принять чрезмерно сильный automated R-F3 verdict.
Stage 3G — variance-reduced stochastic correction
Stage 3G resolves a reproducible nonzero nonlinear D4 stochastic conditional-mean correction using independent-pool control-variate estimation: 24/24 fixed states have positive cross-pool signal, median variance-reduction factor ≈598.6, and Pool-A/Pool-B correction directions are nearly collinear. However, the stronger “predictably low-dimensional” interpretation is not accepted: a trajectory-fraction-only baseline trained on seeds 3–6 reaches cross-replicate skill ≈0.98, matching or exceeding the reported Stage-3G predictor ≈0.971. The archive also contains only postprocessing recovery code, not the exact original scientific sampling/prediction cell. Spectral interpretation remains disallowed. Current priority is independent second-order mechanistic validation and a beyond-clock residual test.
Reason: Separate the robust existence of a nonlinear stochastic mean correction from unsupported Koopman/state-structure and spectral claims, and record the newly identified trajectory-fraction baseline plus reproducibility gap.

Stage 3H — independent mechanistic second-order validation
Independent TARGET/AUDIT pools reproduce the D4 stochastic mean correction. Richardson second-order predictor Q2 achieves pooled cross-replicate skill 0.9842 with seed-bootstrap 95% CI [0.9670,0.9924], no-calibration slope 0.9448, and positive residual skill 0.9035 beyond the best clock baseline. Raw-sample audit shows pooled evidence is strongly weighted toward late trajectory states and statewise amplitude errors remain non-negligible. Result: strong local support for a second-order-dominated Taylor mechanism at eta=0.05, B=128; no spectral inference.
Зафиксировать сильный результат без превращения его в Koopman/spectral claim.
Stage 3I-R — clean independent exact-HVP replication
A fully new independent replication was run with a new dataset subset, new trajectories, new F_new observable, seeds 13–18, fractions 0.25/0.45/0.65/0.85, batch sizes 32/64/128/256/512, fixed-state conditional sampling, and four independent RNG pools. TARGET/AUDIT stochastic corrections replicate. The exact second-order C2 predictor has pooled skill ≈0.9272 with 95% CI ≈[0.8445,0.9556], no-calibration slope ≈0.8291, 6/6 positive seeds at B=128, and C2 batch-scaling exponent ≈-0.9857 with 95% CI ≈[-1.0112,-0.9602]. The run's automated diagnosis remained R4 INCONCLUSIVE because the original float32 finite-difference HVP sanity check gave relative error ≈1.037.
Reason: Preserve the strong independent second-order evidence while not accepting the exact-HVP implementation until the failed numerical sanity check was independently resolved.

Stage 3I-R HVP audit — numerical falsification of the exact second-order contraction
Dedicated audit stage3ir_hvp_audit_20260903T132224Z tested the archived identity C2 = 0.5 H_Phi(theta_bar)[delta,delta] using the original Stage 3I-R states, directions, probes and F_new only. Final verdict: R-H1 — STRONGLY VALIDATED. Two independent exact-autograd HVP routes agree with median relative discrepancy ≈1.31e-16 in float64. Function-value and gradient-based finite differences converge to the exact HVP; pooled median minimum errors are ≈3.17e-8 and ≈4.03e-10 respectively, with gradient-FD convergence slope ≈1.9999. All 3072/3072 directions have minimum FD error <0.25. Archived C2 agrees with recomputed HVP C2 at scale factor 1 with median relative error ≈2.12e-7 and cosine ≈1. The old failed sanity check is explained by catastrophic cancellation of tiny second differences in float32; no missing 1/2, eta, eta^2, sign, or batch scaling factor was found. A minor reporting-label issue remains: decision.json's combined median_float64_fd_min_relative_error is not the literal pooled median of a single route, but this does not affect R-H1.
Reason: Close the exact-HVP numerical gate without promoting the result to Koopman/spectral claims.


Stage 3J — residual beyond validated C2, full repaired analysis
Source run: `stage3j_residual_beyond_c2_20260903T181151Z`; final package analyzed as `stage3j_residual_beyond_c2_20260903T181151Z_analysis_repaired_results.zip`. The heavy scientific generation was interrupted/resumed several times, but checkpoint reuse preserved completed blocks. The final analysis-only repair read 120 completed scientific NPZ blocks (6 seeds × 4 trajectory fractions × 5 batch sizes), did not rerun SGD/gradients/HVPs or generate new pools, fixed only a pandas-Series-to-np.concatenate aggregation bug, and retained PASS provenance to the Stage 3I-R source hashes.

Primary B=128 result across 24 fixed states: pooled independent-pool cross-replicate skill ≈0.143574, pooled cosine ≈0.147394, seed-bootstrap 95% CI for skill ≈[-0.302712, 0.411942], positive seed skills 2/6, positive state-cosine fraction 0.50. Seed skills were negative for seeds 13–16 and positive for seeds 17–18, so no post-hoc subgroup claim is allowed. Across trajectory fractions, residual energy is only about 0.15%–0.40% of C2 energy. Null controls pass.

Batch-scaling diagnostics remain descriptive only: C2 scales very close to B^-1 for all six seeds; residual norms show steeper empirical exponents around -1.40 to -1.64; C4 summaries are near B^-2. These residual/higher-order exponents are not promoted to mechanism claims because the residual itself fails independent replication and the per-scale T3/T4 convergence curves were not retained. The repaired archive therefore cannot authorize J2/J3 higher-order conclusions.

Final verdict: **J1 — NO RESOLVED RESIDUAL**. Scientific interpretation: at the current resolution, the validated local second-order C2 term exhausts the reproducible nonlinear conditional-mean signal. This is not proof that the mathematical remainder is identically zero. No Koopman/EDMD/generator/eigenvalue/spectral claim follows.

Decision: stop attempts to escalate the local residual. Next experiment is Stage 3K, a clean zero-fit out-of-sample test of whether local C2 measurements predict unseen (eta,B) conditional transitions and define a reproducible boundary of validity.
Reason: Convert the strongest supported mechanism into a predictive falsification experiment rather than spend more compute resolving a sub-percent, non-replicating residual.


Stage 3K — zero-fit finite-step prediction, final repaired analysis
Source scientific run: `stage3k_zero_fit_finite_step_prediction_20260904T004119Z`. Final analysis-only repair: `stage3k_zero_fit_finite_step_prediction_20260904T004119Z_analysis_repaired_20260904T073851Z`.

The run used fresh network seeds 31–36, fresh fixed states, eta={0.0125,0.025,0.05,0.075,0.1}, B={32,64,128,256,512}, 256 TARGET + 256 AUDIT draws, and predictions frozen+SHA256-hashed before target generation. No Stage 3I-R/J scientific target arrays were reused. The repair reused the completed Stage 3K scientific artifacts without recomputation and verified prediction-freeze integrity.

The original K5 diagnosis was caused by two analysis bugs. First, condition-wise skill was computed by averaging unstable statewise normalized skill ratios rather than pooled SSE. Second, the frozen-reference baseline contained an extra B_ref factor; at eta_ref=0.05, B_ref=128 it was inflated by 128. The repaired analysis corrected only deterministic postprocessing.

Final verdict: **K1-R — STRONG ZERO-FIT PREDICTION; BOUNDARY NOT REACHED.** Core pooled FULL_C2 skill ≈0.90129 with seed-bootstrap 95% CI ≈[0.69308,0.94905]; full-grid skill ≈0.87908. All 25/25 eta×B conditions have positive pooled skill and bootstrap lower CI >0 and satisfy strong-valid criteria. No tested condition gives a reproducible failure boundary.

The corrected single-reference frozen predictor performs essentially as well as full eta-dependent curvature recomputation: core/full skills ≈0.90227/0.88067; FULL−FROZEN core difference ≈−0.00098 with CI ≈[−0.00435,0.00196]. Isotropic-noise baseline remains weak: core skill ≈0.02009. This supports the practical possibility of measuring C2 once and extrapolating by eta^2/B within the tested regime.

Important heterogeneity: equal-seed core mean/median FULL_C2 skill ≈0.6652/0.8542; seeds 31–32 are weak, and seeds 34–35 carry ≈92.84% of core target energy. Therefore the strong pooled result is not a uniform per-network guarantee.

Decision: Stage 3K is closed positively. Do not rerun it merely to search for a boundary. Next gate is Stage 3L practical downstream prediction from a single reference C2 measurement, with explicit comparison against gradient noise scale and Hessian/projected-noise baselines.
Reason: promote the result from mechanism validation to zero-fit predictive evidence while preserving seed heterogeneity and forbidding universal/practical claims until a downstream consequence is predicted.

Stage 3L — one-shot C2 short-horizon practical materiality
Run: `stage3l_one_shot_c2_short_horizon_materiality_20260904T080455Z`.
Fresh seeds 41–46, fresh states, predictions frozen before TARGET/AUDIT. Original automated verdict: **L4 — OUTCOME UNRESOLVED**. Original H=10 norm-based materiality gave C2 Spearman ≈0.783 with seed-bootstrap CI ≈[0.722,0.823], but direct threshold balanced accuracy ≈0.507 and no reliable superiority over GNS/isotropic/projected-noise baselines. The outcome itself was weakly replicated, so these downstream metrics were not promoted to claims.

Stage 3L-R — debiased analysis-only repair
Run: `stage3l_analysis_repaired_debiased_20260904T122818Z`.
No scientific data were regenerated. Prediction freeze was verified and raw per-trajectory TARGET/AUDIT arrays were reused. The repair introduced the unbiased independent cross-energy estimator `S2_cross = Delta_T^T Delta_A` plus per-pool `||Delta||^2 - tr(Sigma)/n` diagnostics. Final verdict: **LR4 — REPAIR STILL INCONCLUSIVE**. At H=10, positive cross-energy fraction ≈0.50463, pool-debiased sign agreement ≈0.50926, repaired-resolved fraction = 0, strict-resolved fraction = 0, and median original norm materiality / cross-fitted materiality ≈6.277. Therefore the original mean-shift endpoint was substantially Monte-Carlo inflated and the true H=10 conditional mean is not resolved at this budget. No valid conclusion can be drawn about failure of `H*C2`.

Decision: close the immediate mean-shift batch-selector branch and move to Stage M1, where the target is finite-horizon stochastic covariance rather than a tiny conditional mean. Stage M1 must first validate i.i.d. tangent covariance propagation before any random-reshuffling/non-Markovian extension.


Stage M1 — finite-horizon covariance propagation under i.i.d. minibatching
Run: `stage_m1_finite_horizon_covariance_iid_20260904T164751Z`.

Full protocol used fresh seeds 51–56, fractions 0.25/0.55/0.85, eta={0.025,0.05,0.075,0.10}, B={16,32,64,128,256,512}, H={1,5,10}, 128 TARGET + 128 AUDIT nonlinear trajectories per condition, 256 local-noise samples, and 64 tangent-prediction draws. Predictions were frozen and hashed before TARGET/AUDIT generation. The predictor uses centered one-example gradient deviations, exact float64 HVPs and matrix-free tangent propagation along the matched deterministic full-gradient path. TARGET/AUDIT use i.i.d. minibatches with replacement and recompute gradients at the current stochastic parameters.

Final verdict: **M1 — FINITE-HORIZON COVARIANCE PROPAGATION SUPPORTED.** TARGET/AUDIT covariance replication is strong at H=1,5,10. H=10 predictor: mean Frobenius skill ≈0.92668 (seed-bootstrap 95% CI ≈[0.91548,0.93812]), mean matrix cosine ≈0.97920, trace relative error ≈0.1143, top-eigenvalue relative error ≈0.1663, top-1 eigenspace overlap ≈0.9776. All six seed-level H=10 skills are high and positive (≈0.908–0.947).

Baseline decomposition at H=10: C_pred−no-propagation skill ≈+0.64999 [0.62177,0.67138]; C_pred−isotropic ≈+0.91477 [0.90191,0.92855]; C_pred−frozen-geometry ≈+0.01396 [0.00187,0.02505]. Thus finite-horizon accumulation/propagation and anisotropic noise geometry are decisive; moving deterministic geometry adds a small but reproducible increment. The scalar B3/GNS-like parameter-noise score has Spearman ≈0.98068 with TARGET trace, so total variance magnitude alone is not the unique contribution.

A prior execution crashed during figure generation with `KeyError('target_trace')` after the scientific artifacts were already generated; the failure remains archived as `runtime_failure.json`. The final completion used corrected/resume-safe analysis/reporting. Preserve this provenance note.

Decision: close M1 positively and advance to a preregistered correlated-sampling test. Do not yet claim random-reshuffling memory, non-Markovianity, optimizer memory, universality or generalization effects.
