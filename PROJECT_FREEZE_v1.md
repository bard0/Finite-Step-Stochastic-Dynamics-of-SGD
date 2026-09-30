# PROJECT_FREEZE_v1

**Freeze date:** 2026-09-30  
**Public status:** completed portfolio research phase  
**Repository line:** finite-step stochastic dynamics of SGD

## Frozen v1 scope

v1 includes the research line from the original spectral/noise question through:

- controlled spectral perturbation tests;
- additive-noise falsification;
- state-dependent noise-geometry analysis;
- exact scalar mean-square stability construction;
- M9 controlled predictor benchmark;
- repaired temporal-covariance branch and its downgrade;
- G8.10 higher-order neural transfer test and confirmatory negative verdict;
- late finite-step closure proofs as archived theory frontier, without promotion to a general theorem.

## Final headline claims

1. An explicit scalar finite-sum construction shows low-order descriptor insufficiency for exact finite-step mean-square stability.
2. Controlled M9 tests support predictive value of state-dependent noise geometry for matched-system stability and sharpness separation.
3. Additive zero-mean noise is not a generic spectral-shift mechanism in the controlled setting.
4. Universal centered temporal-covariance “memory” is not a valid ordinary-iid SGD mechanism.
5. The preregistered regime-robust neural incremental-value claim for the mixed fourth derivative descriptor failed.
6. Higher-order/moving-reference closure remains a research frontier, not a v1 conclusion.

## Evidence classes

- **Analytical:** exact scalar stability construction; additive control; iid filtration correction.
- **Controlled numerical:** Duffing validation; M9 predictor benchmark.
- **Confirmatory negative:** G8.10-B4 neural incremental-value test.
- **Exploratory:** eta heterogeneity and late higher-order coupling/closure constructions.
- **Inconclusive:** paper-faithful Liao moving-reference subset with insufficient eligible independent seed groups.

## Frozen public artifacts

- `README.md`
- `FINAL_RESEARCH_SUMMARY.md`
- `docs/current_research_state.md`
- `docs/claims_and_evidence.md`
- `docs/portfolio_key_results.md`
- `research_history/README.md`
- `experiments/M9/`
- `experiments/G8_10/`
- `CHANGELOG.md`
- canonical large archives and proof logs on project storage

## v2 boundary

The following are explicitly **not required to complete v1** and belong to a possible v2:

- moving-reference / moving-PGD spectral-closure theorem;
- long-horizon remainder control;
- proof that a compact coupling quotient remains sufficient for a fixed smooth finite-sum objective;
- multidimensional/general-network transfer of the exact scalar stability theorem;
- prospective neural confirmation of regime-dependent higher-order effects;
- external theorem-by-theorem priority review sufficient for a publication claim.

No v1 claim may be retroactively strengthened using exploratory v2 work without a new preregistered or theorem-audited evidence update.

## Stop rule

The v1 research line is considered complete. New hypotheses should open a new milestone/version rather than extend the v1 claim ledger indefinitely.


## Frozen reference

- frozen branch: `freeze-v1.0`
- frozen commit: `532bdf8c4b57749a9cc9bc02056f48c072808819`
- portfolio freeze bundle SHA256: `13b5b087312e2d157761df41c58ad4ea00abf4af55f19291664cbe521cc18a08`

The local freeze bundle is a compact portfolio package; the canonical full experiment archives remain in project storage.
