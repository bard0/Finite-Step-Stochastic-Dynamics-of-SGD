# Reproducibility

This repository preserves scientific provenance of finite-step SGD experiments.

## Archived experiments

Exact execution scripts are retained when available. Refactored implementations should not replace archived experiment sources.

## Required experiment artifacts

Each experiment should preserve:

- source code;
- configuration;
- random seeds;
- logs;
- metrics;
- figures;
- checkpoints when applicable;
- final archive and checksum.

## Scientific controls

Before accepting a claim:

1. define a falsification test;
2. compare against relevant prior work;
3. specify baselines and controls;
4. report limitations.

Large generated artifacts are distributed separately according to `ARTIFACTS.md`.
