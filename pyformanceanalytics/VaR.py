"""The PerformanceAnalytics VaR function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.VaR import VaR as RVaR
from .var_clean import VaRClean
from .var_method import VaRMethod
from .var_portfolio_method import VaRPortfolioMethod


def VaR(
    R: (pd.DataFrame | None) = None,
    p: float = 0.95,
    method: (str | VaRMethod | None) = None,
    clean: (str | VaRClean | None) = None,
    portfolio_method: (str | VaRPortfolioMethod | None) = None,
    weights: (pd.DataFrame | None) = None,
    mu: (pd.DataFrame | float | None) = None,
    sigma: (pd.DataFrame | float | None) = None,
    m3: (pd.DataFrame | float | None) = None,
    m4: (pd.DataFrame | float | None) = None,
    invert: bool = False,
    SE: bool = False,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate VaR."""
    if method is None:
        method = VaRMethod.MODIFIED
    if clean is None:
        clean = VaRClean.NONE
    if portfolio_method is None:
        portfolio_method = VaRPortfolioMethod.SINGLE
    if backend == Backend.R:
        if isinstance(method, VaRMethod):
            method = method.value
        if isinstance(clean, VaRClean):
            clean = clean.value
        if isinstance(portfolio_method, VaRPortfolioMethod):
            portfolio_method = portfolio_method.value
        return RVaR(
            method,
            clean,
            portfolio_method,
            R=R,
            p=p,
            weights=weights,
            mu=mu,
            sigma=sigma,
            m3=m3,
            m4=m4,
            invert=invert,
            SE=SE,
        )
    raise NotImplementedError(f"Backend {backend.value} not implemented for VaR")
