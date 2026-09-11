# Finite-Sample Stochastic Stability Boundary

## Status

Active adjacent theory branch; not yet a confirmed theorem.

## Question

Can finite data reliably determine stochastic stability near a spectral boundary when the stability operator itself is consistently estimable?

For a lifted second-moment operator `M`, stability is governed by `rho(M)<1`. The working statistical hypothesis is that the binary boundary functional can be non-regular under local alternatives near `rho(M)=1`, so point operator convergence may coexist with unreliable stable/unstable classification.

## Target contribution

- characterize local alternatives near the boundary;
- establish when uniform binary classification is impossible or poorly conditioned;
- construct calibrated uncertainty intervals or `stable / unstable / uncertain` rules;
- connect the result to approximation selection for finite-step SGD.

## Non-claims

- not a new stochastic stability operator;
- not generic spectral learning theory;
- not a claim that stability thresholds are unknown in quadratic SGD.

The novelty target is the finite-sample reliability of the boundary decision.
