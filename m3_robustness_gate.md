# Memory update — after Stage M2 / before Stage M3

## Current status

Stage M1 established zero-fit finite-horizon stochastic covariance prediction under i.i.d. minibatching.

Stage M2 established that random reshuffling produces reproducible finite-horizon covariance changes beyond matched one-step without-replacement marginals. The causal comparison used:
- RR: permutation-based sequential batches;
- IND_SUBSET: independently sampled without-replacement batches.

Current accepted scientific direction:

finite-horizon stochastic covariance geometry of SGD.

## Main conclusions

Do not return to:
- Koopman closure claims;
- spectral universality claims;
- C2 mean-shift batch selector;
- practical batch-size optimization claims.

The strongest supported object is covariance geometry, not conditional mean shift.

## Stage M3 active priority

Goal:
test whether finite-horizon covariance propagation is robust beyond the original small-network/dataset platform.

M3 is a robustness/falsification gate, not a new theory.

Required axes:
1. architecture shift;
2. dataset shift.

Keep unchanged:
- prediction freeze;
- deterministic tangent propagation;
- HVP machinery;
- function-space covariance target;
- TARGET/AUDIT replication;
- seed bootstrap.

Main question:

Is
gradient-noise covariance + deterministic tangent propagation
a general SGD stochastic-geometry mechanism, or an artifact of one experimental setup?

Allowed future claims depend on M3 outcome.

## Next stages

Only after robustness:
- optimizer state / momentum;
- adaptive methods;
- broader SGD dynamics.

Do not interpret RR temporal covariance as generic SGD memory.
