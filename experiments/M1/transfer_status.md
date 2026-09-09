# M1 artifact transfer status

## Current state

Public transfer is complete for the normal Git-history layer of M1.

Included in the repository:

- portable runnable source under `code/`;
- public configuration;
- compact completed-run summaries;
- source provenance and reproducibility notes.

The portable source preserves the scientific calculation while replacing environment-specific storage assumptions with configurable local roots.

## External artifacts

Large raw trajectories, checkpoints, generated tensors, caches, and full archives remain outside normal Git history. They are retained in the research archive and are not required for understanding the public claim boundary.

## Public claim boundary

M1 supports zero-fit finite-horizon covariance prediction from local anisotropic gradient noise propagated through deterministic geometry in the tested small-network i.i.d.-minibatch regime. It does not support claims about temporal ordering, universal SGD behavior, generalization, or optimal batch size.
