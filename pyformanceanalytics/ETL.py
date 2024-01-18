"""The PerformanceAnalytics ETL function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import numpy as np
import pandas as pd

from .backend.backend import Backend
from .backend.R.ETL import ETL as RETL
from .ETL_clean import ETLCLean
from .ETL_method import ETLMethod
from .ETL_portfolio_method import ETLPortfolioMethod


def ETL(
    R: pd.DataFrame,
    p: float = 0.95,
    method: (str | ETLMethod | None) = None,
    clean: (str | ETLCLean | None) = None,
    portfolio_method: (str | ETLPortfolioMethod | None) = None,
    weights: (list[float] | None) = None,
    mu: (list[float] | None) = None,
    sigma: (np.ndarray | None) = None,
    m3: (np.ndarray | None) = None,
    m4: (np.ndarray | None) = None,
    invert: bool = True,
    operational: bool = True,
    SE: bool = False,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate ETL."""
    if method is None:
        method = ETLMethod.MODIFIED
    if clean is None:
        clean = ETLCLean.NONE
    if portfolio_method is None:
        portfolio_method = ETLPortfolioMethod.SINGLE
    if backend == Backend.R:
        if isinstance(method, ETLMethod):
            method = method.value
        if isinstance(clean, ETLCLean):
            clean = clean.value
        if isinstance(portfolio_method, ETLPortfolioMethod):
            portfolio_method = portfolio_method.value
        return RETL(
            R,
            method,
            clean,
            p=p,
            weights=weights,
            mu=mu,
            sigma=sigma,
            m3=m3,
            m4=m4,
            invert=invert,
            operational=operational,
            SE=SE,
        )
    raise NotImplementedError(f"Backend {backend.value} not implemented for ETL")
