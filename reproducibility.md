# Reproducibility

## Exact scripts

Files named `run_exact.py` are preserved from archived experiment outputs with only the public repository filename changed. Their scientific code is not refactored.

Several scripts were written as single-cell Google Colab programs and assume `/content` paths and, in some cases, Google Drive mounting.

## Included artifacts

This repository contains compact decision files, configurations, summary tables, provenance reports, and selected audit outputs.

Large raw trajectory arrays, checkpoints, tensors, and multi-gigabyte result archives are intentionally excluded from the Git repository. They should be distributed through a release asset or external data archive.

## Recommended environment

- Python 3.11
- PyTorch
- torchvision
- NumPy
- SciPy
- pandas
- Matplotlib

Use `make check` to perform a syntax and public-release scan.
