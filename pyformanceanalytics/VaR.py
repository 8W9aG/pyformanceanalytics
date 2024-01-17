"""The PerformanceAnalytics VaR function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame_or_float
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .var_clean import VaRClean
from .var_method import VaRMethod
from .var_portfolio_method import VaRPortfolioMethod
from .xts import xts_from_df


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
) -> pd.DataFrame | float:
    """Calculate VaR."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if method is None:
        method = VaRMethod.MODIFIED
    if clean is None:
        clean = VaRClean.NONE
    if portfolio_method is None:
        portfolio_method = VaRPortfolioMethod.SINGLE
    if isinstance(method, VaRMethod):
        method = method.value
    if isinstance(clean, VaRClean):
        clean = clean.value
    if isinstance(portfolio_method, VaRPortfolioMethod):
        portfolio_method = portfolio_method.value
    with ro.local_context() as lc:
        return as_data_frame_or_float(
            ro.r("VaR").rcall(  # type: ignore
                (
                    ("R", None if R is None else xts_from_df(R)),
                    ("p", p),
                    ("method", method),
                    ("clean", clean),
                    ("portfolio_method", portfolio_method),
                    ("weights", weights),
                    ("mu", mu),
                    ("sigma", sigma),
                    ("m3", m3),
                    ("m4", m4),
                    ("invert", invert),
                    ("SE", SE),
                ),
                lc,
            ),
            lc,
        )
