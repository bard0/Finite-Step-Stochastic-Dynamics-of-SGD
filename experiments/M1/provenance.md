# M1 provenance

## Purpose

M1 establishes the finite-horizon covariance propagation baseline for the project.

## Scientific role

The experiment studies whether a local stochastic description can predict finite-step covariance evolution through deterministic propagation dynamics.

## Preserved information

The public repository should preserve:

- experiment configuration;
- random seeds;
- model definition;
- evaluation metrics;
- generated summaries;
- provenance information.

## Artifact policy

Large generated artifacts are stored separately from the source repository. The repository contains compact reproducibility information and references to the corresponding experiment records.

## Claim boundary

M1 supports the tested finite-horizon covariance prediction setting. It does not by itself establish a universal description of stochastic gradient descent dynamics.
