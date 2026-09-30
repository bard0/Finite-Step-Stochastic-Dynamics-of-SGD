# Portfolio Key Results

These are the three results recommended for a short talk, portfolio page, or interview deck.

## Figure 1 — Controlled spectral perturbation works when assumptions are enforced

**Visual:** predicted versus measured spectral shift in the controlled Duffing experiment.

**Caption:**  
*In a controlled stochastic Duffing system, the perturbative spectral predictor closely tracks directly measured spectral shifts (mean absolute error about \(1.5\times10^{-7}\), median relative error about \(2.5\times10^{-3}\), Spearman correlation about \(0.999\)). The result validates the computational machinery in a regime where model assumptions are deliberately satisfied; it is not a universal neural-SGD theorem.*

**Message:** the project began with a mechanism that genuinely worked in a controlled setting.

## Figure 2 — Noise geometry predicts matched finite-step stability

**Visual:** grouped bars or predicted-vs-true comparison for M9, highlighting matched \(\Delta\eta_c\) and \(\Delta S\).

**Caption:**  
*In the controlled M9 family, a state-dependent noise-geometry descriptor strongly improves prediction of matched-system differences: \(R^2=0.8485\) for \(\Delta\eta_c\) and \(R^2=0.9835\) for matched sharpness-gap differences. Absolute sharpness is already well explained by the projected-noise baseline, so the incremental result is specifically about descriptor sufficiency and matched separation.*

**Message:** the strongest positive v1 result is not “more noise matters,” but “how noise changes with state can matter beyond simpler closures.”

## Figure 3 — A sophisticated neural descriptor fails the preregistered robustness gate

**Visual:** pooled and eta-stratified MAE gain for G8.10-B4, with the bootstrap interval crossing zero.

**Caption:**  
*Adding the mixed fourth directional derivative \(\chi_{mix}\) reduced pooled MAE by \(4.70\%\), but the seed-group bootstrap interval crossed zero and the effect changed sign across learning-rate regimes (+14.76% at \(\eta=0.018\), -2.66% at \(\eta=0.020\)). The preregistered regime-robust claim was therefore rejected.*

**Message:** negative results were used to narrow the theory rather than hidden or post-hoc rescued.
