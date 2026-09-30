# Project Overview

This repository records a completed v1.0 research project on finite-step SGD.

## Question

The project began with spectral perturbation ideas and ended with a more specific question:

**Which stochastic descriptors are sufficient to determine a finite-step stability or dynamical quantity?**

## What survived

- controlled spectral perturbation works well in the Duffing testbed when its assumptions are enforced;
- additive noise amplitude alone is not a generic spectral-shift mechanism;
- state-dependent noise geometry can change exact mean-square stability even when simpler local descriptors match;
- M9 supports this effect in controlled matched-system prediction;
- a higher-order neural descriptor, chi_mix, did not pass the preregistered cross-regime test.

## What was dropped

The project no longer uses a universal temporal-covariance mechanism as its main explanation for iid SGD, and it does not treat a formal higher-order expansion as evidence of practical relevance by itself.

## Status

v1.0 is complete. Moving-reference theory, long-horizon control, multidimensional transfer, and new prospective neural tests are separate future-work questions.
