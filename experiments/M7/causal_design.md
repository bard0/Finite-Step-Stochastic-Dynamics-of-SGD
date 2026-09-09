# M7 — Causal design

## Question

Does temporal ordering of gradient noise contain information beyond one-step marginal statistics?

## Controls

The experiment compares:

1. original temporal ordering;
2. shuffled ordering with preserved samples;
3. independent controls with matched marginal statistics.

## Required interpretation

The temporal contribution is attributed only to the extent that the real ordering differs from controls that preserve one-step distributions.

## Limitations

The result is restricted to the tested systems, observables and finite horizons. It should not be interpreted as a universal characterization of SGD dynamics.
