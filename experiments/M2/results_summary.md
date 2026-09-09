# M2 results summary

## Question

Does temporal organization of stochastic gradients provide additional information about finite-horizon covariance geometry beyond matched one-step statistics?

## Experimental design

M2 compares random reshuffling against independently redrawn without-replacement subsets. At each fixed step the two schemes share the same one-step subset marginal; the intervention changes cross-time organization.

The central object is

\[
K_{st}=\operatorname{Cov}(\xi_s,\xi_t).
\]

The full temporal predictor retains cross-time covariance, while the matched diagonal baseline retains the one-step covariance and removes off-diagonal temporal structure.

## Completed-run diagnosis

The archived full run returned **M2-1**. M1 source integrity, prediction freezing, matched one-step marginal checks, and the analytic finite-population temporal-covariance identity audit passed. A legacy finite-draw Monte Carlo formula diagnostic did not pass; it is retained as a negative diagnostic rather than used as the final identity check.

At horizon H=10, the archived full temporal RR predictor had mean Frobenius skill **0.95408**, with seed-bootstrap 95% interval **[0.94819, 0.96155]**.

## Strongest allowed interpretation

In the tested small-CNN regime, random reshuffling produces a reproducible finite-horizon covariance change beyond matched one-step without-replacement marginals, and explicit temporal per-example gradient-noise correlations predict that change zero-fit under deterministic tangent propagation.

## Claim boundary

This does not establish a universal memory mechanism, universal non-Markovianity, a generalization advantage of random reshuffling, optimizer memory, or a universal SGD law. Cross-architecture and cross-dataset validation is required before broadening the claim.

See `results/decision_report.md` for the archived decision record. Large condition-level tables, raw arrays, gradient banks and checkpoints remain external artifacts.
