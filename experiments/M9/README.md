# M9_eos_comparison

## Frozen predictors

- Model 0: `eta_c=2/lambda`, `DeltaS=0`.
- Model 1: `eta_c=2/lambda`; sharpness uses only `eta`, curvature, and `sigma_u^2=Sigma(0)`. It has no `G_Sigma` argument.
- Model 2: `eta_c=2*lambda/(lambda^2+G_Sigma)`; sharpness uses the corresponding mean-square denominator `2*lambda-eta*(lambda^2+G_Sigma)`.

No model is fit to empirical targets. Model 2 receives no empirical threshold, observed sharpness, stability label, or post-run tuning.

## Measurements and leakage control

Empirical thresholds use 12 fixed EST seeds. Stationary metrics use 12 disjoint fixed EVAL seeds. Each seed contains 12 simultaneous trajectories and is treated as the bootstrap cluster. Evaluation eta is fixed from Model 2 descriptors before measurement, never from empirical eta_c.

The empirical classifier uses only finite trajectories, the frozen absolute cutoff, complete stationary sampling, the frozen second-moment cutoff, and the stable-fraction rule. Predictor values do not enter classification.

This continuous-noise 1D experiment is not called an EoSS Batch-Sharpness experiment. Genuine mini-batch Batch Sharpness belongs to a separate finite-sum control.

## Controls

A and B share lambda, gamma, sigma, Sigma(0), sigma_u^2, eta, x0, seeds, trajectory count, and duration. Their normal streams are independent. The only stochastic-law intervention is `G_Sigma`: 0 for A and c^2 for B.

## Predictor metrics

- system_level_eta_c | Model0/1: MAE=0.6741022, RMSE=0.9052738, R2=-1.2446048
- system_level_eta_c | Model2: MAE=0.2075223, RMSE=0.2839890, R2=0.7791064, Spearman=0.8714457
- system_level_DeltaS | Model1: MAE=0.00070698, R2=0.9518760, Spearman=0.9847636
- system_level_DeltaS | Model2: MAE=0.00017741, R2=0.9942580, Spearman=0.9998160
- system_difference_Delta_eta | Model0/1: MAE=0.8524137, R2=-2.2404956
- system_difference_Delta_eta | Model2: MAE=0.1475579, R2=0.8484967, Spearman=0.9543159
- system_difference_DeltaS | Model0/1: MAE=0.00118755, R2=-0.1681691
- system_difference_DeltaS | Model2: MAE=0.00012412, R2=0.9834661, Spearman=0.9776999

The full compact metric table is in `predictor_metrics.csv`.

## Audit

- Model1_uses_G_Sigma: False
- Model2_uses_empirical_threshold: False
- A_B_sigma_u2_equal_by_construction: True
- prediction_measurement_leakage: False
- EST_EVAL_seeds_disjoint: True
- EST_seed_count: 12
- EVAL_seed_count: 12
- CI_unit: seed_cluster
- CI_method: percentile_seed_cluster_bootstrap
- eta_grid_fixed_before_simulation: True
- empirical_classifier_uses_predictors: False

## Canonical artifacts

The project Drive retains `config.json`, `results.csv`, `predictor_metrics.csv`, figures, logs, checkpoint, manifest, README, and a verified ZIP archive.
