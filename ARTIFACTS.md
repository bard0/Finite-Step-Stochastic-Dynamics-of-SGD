# Data and artifact policy

The working project contains result archives ranging from tens of megabytes to multiple gigabytes.

To keep the Git repository practical, version 1.0 includes:
- exact execution scripts where directly recoverable;
- experiment configuration and decision files;
- summary CSV tables;
- provenance and numerical-audit reports.

Excluded:
- raw trajectory blocks;
- model checkpoints;
- large `.pt`, `.npz`, and generated cache trees;
- multi-gigabyte result archives.

These should be attached to a tagged release or deposited in an external archival service if full public reproducibility is required.
