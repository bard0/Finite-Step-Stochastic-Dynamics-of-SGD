# Research roadmap

## Current priority

1. Consolidate finite-step SGD operator theory.
2. Formalize descriptor sufficiency and insufficiency questions.
3. Complete causal temporal-ordering validation.
4. Connect controlled stochastic systems with neural SGD experiments.
5. Prepare theorem-level and experiment-level evidence tables.

## Current theoretical direction

The central question has shifted from whether stochastic noise matters to:

Can finite-step SGD dynamics be characterized by a small set of classical stochastic descriptors, or does the discrete stochastic operator contain additional information?

Current candidate direction:

- exact finite-step operator analysis;
- comparison with diffusion approximations;
- testing sufficiency of edge-of-stability descriptors;
- identifying missing stochastic information.

## Remaining validation gates

### M7 / T1

Test whether temporal organization itself causes measurable changes while preserving one-step marginals.

Controls:
- original ordering;
- temporal shuffle;
- independent marginal sampling.

### T2

Theoretical and empirical extension toward descriptor insufficiency and spectral consequences.

## Claim discipline

The project should not move from predictive correlation to mechanism claim without causal controls.

A negative result is considered valuable if it rules out an attractive but unsupported explanation.
