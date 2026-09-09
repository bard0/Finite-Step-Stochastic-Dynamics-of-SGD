# M1 final diagnosis

## Required answers

- prediction freeze passed: YES
- fresh scientific data: YES
- TARGET/AUDIT covariance replication at H=1: True
- at H=5: True
- at H=10: True
- C_pred H=10 Frobenius skill: 0.9266836191417097
- seed-bootstrap 95% CI: [0.9154807016457983, 0.9381187451061841]
- matrix cosine / trace error / top-eigenvalue error / top-eigenspace overlap: see `horizon_summary.csv`
- no-propagation, frozen-geometry, isotropic and scalar-noise baselines: see `baseline_comparison.csv`
- should advance to temporally correlated minibatch sampling: YES

## Strongest allowed claim

In this tested small-network i.i.d.-minibatch regime, finite-horizon covariance can be predicted zero-fit from local anisotropic gradient noise propagated through deterministic geometry.

## Forbidden claims

No claims about random reshuffling, temporal noise memory, non-Markovian SGD, optimizer memory, universality, large-model validity, generalization, or optimal batch size.
