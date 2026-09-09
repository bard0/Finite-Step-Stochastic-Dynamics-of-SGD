# M1 artifact transfer status

## Current state

The public repository contains the experiment description and reproducibility requirements for M1.

## Artifact migration policy

Before adding executable sources or generated artifacts, each file is checked for:

- reproducibility information;
- removal of local environment paths;
- removal of temporary execution metadata;
- absence of private workflow material;
- consistency with the public claim level.

## Pending public artifacts

The following items should be added from the archived research storage when the exact source artifact is available:

- experiment configuration;
- executable source;
- compact result summaries;
- provenance information.

Large raw trajectories, checkpoints and generated caches remain external release artifacts.
