# M7 public source provenance

The working project retains the executed M7 source and its resumed execution source. A portable public source was prepared from the latest consolidated execution source.

Portability changes are limited to:

- replacing notebook/storage-specific runtime assumptions with a configurable project root;
- simplifying source snapshot capture for ordinary Python execution;
- removing environment-specific storage metadata;
- preserving the frozen experiment configuration, causal replay modes, metrics, checkpoints and output logic.

Prepared public source SHA-256:

`016e3c3c3d87351475c0ad1c841aebbb97e17b0a3e2db5cf90e7930930d3cbc2`

The exact archived execution source remains part of the experiment provenance. The public configuration and controlled M7.1 summary are included in this directory; large trajectory and checkpoint artifacts remain outside normal Git history.
