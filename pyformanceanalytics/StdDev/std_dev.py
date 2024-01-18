"""The PerformanceAnalytics StdDev function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.StdDev.std_dev import StdDev as RStdDev
from .std_dev_clean import StdDevClean
from .std_dev_method import StdDevMethod
from .std_dev_portfolio_method import StdDevPortfolioMethod


def StdDev(
    R: pd.DataFrame,
    clean: (str | StdDevClean | None) = None,
    portfolio_method: (str | StdDevPortfolioMethod | None) = None,
    weights: (list[float] | None) = None,
    mu: (list[float] | None) = None,
    sigma: (list[float] | None) = None,
    use: (str | None) = None,
    method: (str | StdDevMethod | None) = None,
    SE: bool = False,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate StdDev."""
    if clean is None:
        clean = StdDevClean.NONE
    if portfolio_method is None:
        portfolio_method = StdDevPortfolioMethod.SINGLE
    if method is None:
        method = StdDevMethod.PEARSON
    if backend == Backend.R:
        if isinstance(clean, StdDevClean):
            clean = clean.value
        if isinstance(portfolio_method, StdDevPortfolioMethod):
            portfolio_method = portfolio_method.value
        if isinstance(method, StdDevMethod):
            method = method.value
        return RStdDev(
            R,
            clean,
            portfolio_method,
            method,
            weights=weights,
            mu=mu,
            sigma=sigma,
            use=use,
            SE=SE,
        )
    raise NotImplementedError(f"Backend {backend.value} not implemented for StdDev")
