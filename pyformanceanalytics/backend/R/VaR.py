"""The PerformanceAnalytics VaR function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def VaR(
    method: str,
    clean: str,
    portfolio_method: str,
    R: (pd.DataFrame | None) = None,
    p: float = 0.95,
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
    with ro.local_context() as lc:
        return as_data_frame(
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
