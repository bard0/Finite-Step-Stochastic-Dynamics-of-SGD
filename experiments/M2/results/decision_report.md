FINAL DIAGNOSIS: M2-1

# Stage M2 decision report

- M1 source integrity passed?: YES
- prediction freeze before new stochastic outcomes?: YES
- matched one-step marginal audit passed?: True
- analytic RR K_st exact identity audit passed?: True
- legacy finite-draw MC formula diagnostic passed?: False
- RR TARGET/AUDIT covariance replication at H=1,2,4,8,10,16?: See archived covariance replication table
- IND TARGET/AUDIT covariance replication?: See archived covariance replication table
- DeltaC TARGET/AUDIT replication?: See archived temporal-difference replication table
- fraction of conditions with resolved temporal difference?: See archived delta-covariance results
- median relative temporal-effect magnitude?: See archived delta-covariance results and seed summary
- RR full predictor H=10 skill + CI?: [{'mean': 0.9540795978311533, 'ci_low': 0.9481913831582586, 'ci_high': 0.9615509434353572}]
- RR full predictor matrix cosine?: See archived condition results
- diagonal baseline skill?: See archived condition results
- RR-minus-diagonal bootstrap delta?: See archived bootstrap summary
- DeltaC prediction skill + CI?: See archived bootstrap summary
- DeltaC matrix cosine?: See archived delta-covariance results
- epoch-end trace ratio observed vs predicted?: See archived epoch-structure summary
- equal-seed mean/median?: See archived seed summary
- any seed concentration problem?: See archived per-example noise diagnostics and seed summary
- frozen-time RR baseline?: See archived condition results
- does temporal correlation add predictive information beyond one-step marginals?: M2-1
- strongest allowed claim?: Verdict-controlled; see below
- forbidden claims?: No universal memory, novelty, generalization, optimizer-memory, or RR-superiority claims.
- should next stage move to momentum/optimizer memory or first test another architecture/dataset?: FIRST TEST ANOTHER ARCHITECTURE/DATASET

## Strongest allowed claim

In the tested small-CNN regime, RR induces a reproducible finite-horizon covariance change beyond matched one-step WOR marginals, and explicit temporal per-example gradient-noise correlations predict that change zero-fit under deterministic tangent propagation.

## Forbidden claims

Do not claim discovery of SGD memory, first RR theory, universal non-Markovianity, RR generalization benefit, optimizer memory, or a universal law.
