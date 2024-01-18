"""The PerformanceAnalytics StdDev function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.StdDev.std_dev import StdDev as RStdDev


def StdDev(
    R: pd.DataFrame,
    clean: (str | None) = None,
    portfolio_method: (str | None) = None,
    weights: (list[float] | None) = None,
    mu: (list[float] | None) = None,
    sigma: (list[float] | None) = None,
    use: (str | None) = None,
    method: (str | None) = None,
    SE: bool = False,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate StdDev."""
    if backend == Backend.R:
        return RStdDev(
            R,
            clean=clean,
            portfolio_method=portfolio_method,
            weights=weights,
            mu=mu,
            sigma=sigma,
            use=use,
            method=method,
            SE=SE,
        )
    raise NotImplementedError(f"Backend {backend.value} not implemented for StdDev")
