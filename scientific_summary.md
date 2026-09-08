# Scientific summary

## Central question

The project asks which aspects of finite-step stochastic SGD dynamics can be predicted from measurable local geometry and gradient-noise structure, and where those local descriptions fail.

The project moved away from a broad claim of a universal spectral theory of SGD after falsification and literature audits. The strongest supported line is now finite-step conditional and covariance prediction.

## Experimental progression

### Stage 3I-R: exact second-order mechanism

A clean independent replication validated the local second-order finite-step correction. A dedicated HVP audit reported agreement between independent automatic-differentiation routes and finite-difference checks, with the result explicitly restricted to the archived local protocol.

### Stage 3J: residual gate

After subtracting the validated second-order term, the residual did not independently replicate above seed-bootstrap uncertainty. The repaired result therefore does not support escalation to a higher-order or spectral interpretation.

### Stage 3K: zero-fit prediction

Predictions were frozen before independent target generation on fresh seeds and a finite learning-rate/batch-size grid. The archived result supports strong held-out zero-fit prediction in the tested regime, while retaining substantial seed heterogeneity and explicitly forbidding universal claims.

### Stage M1: finite-horizon covariance

The target changed from a small conditional mean shift to the covariance of function-space stochastic deviations. Under i.i.d. minibatching, local anisotropic gradient-noise covariance propagated through deterministic tangent geometry predicted finite-horizon covariance with high skill in the tested small-CNN regime.

### Stage M2: temporally correlated random reshuffling

The archived M2 decision reports that, in the tested small-CNN regime, random reshuffling produces a reproducible finite-horizon covariance change beyond matched one-step without-replacement marginals, and that explicit temporal per-example gradient-noise correlations predict the change zero-fit under deterministic tangent propagation.

### Stage M3

The next robustness gate is architecture and dataset shift. It is a falsification stage rather than a new-theory claim.

## Claim discipline

The repository does not claim:
- a first finite-step theory of SGD;
- a first discrete SGD operator;
- a first projected-noise mechanism;
- universal non-Markovianity;
- universal spectral closure;
- universal batch-size prescriptions.

Claims are limited to the exact archived experimental regimes.
