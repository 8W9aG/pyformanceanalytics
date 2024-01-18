"""The PerformanceAnalytics ETL function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import numpy as np
import pandas as pd
from rpy2 import robjects as ro

from .ETL_clean import ETLCLean
from .ETL_method import ETLMethod
from .ETL_portfolio_method import ETLPortfolioMethod
from .r_df import as_data_frame
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


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
) -> pd.DataFrame:
    """Calculate ETL."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if method is None:
        method = ETLMethod.MODIFIED
    if clean is None:
        clean = ETLCLean.NONE
    if portfolio_method is None:
        portfolio_method = ETLPortfolioMethod.SINGLE
    if isinstance(method, ETLMethod):
        method = method.value
    if isinstance(clean, ETLCLean):
        clean = clean.value
    if isinstance(portfolio_method, ETLPortfolioMethod):
        portfolio_method = portfolio_method.value
    with ro.local_context() as lc:
        with (
            ro.default_converter + ro.numpy2ri.converter + ro.pandas2ri.converter  # type: ignore
        ).context():
            return as_data_frame(
                ro.r("ETL").rcall(  # type: ignore
                    (
                        ("R", xts_from_df(R)),
                        ("p", p),
                        ("method", method),
                        ("clean", clean),
                        (
                            "weights",
                            None
                            if weights is None
                            else ro.vectors.FloatVector(weights),
                        ),
                        ("mu", None if mu is None else ro.vectors.FloatVector(mu)),
                        ("sigma", sigma),
                        ("m3", m3),
                        ("m4", m4),
                        ("invert", invert),
                        ("operational", operational),
                        ("SE", SE),
                    ),
                    lc,
                ),
                lc,
            )
