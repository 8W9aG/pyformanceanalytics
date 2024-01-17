"""The PerformanceAnalytics StdDev function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame_or_float
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


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
) -> pd.DataFrame | float:
    """Calculate StdDev."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if clean is None:
        clean = "none"
    if portfolio_method is None:
        portfolio_method = "single"
    if use is None:
        use = "everything"
    if method is None:
        method = "pearson"
    with ro.local_context() as lc:
        return as_data_frame_or_float(
            ro.r("StdDev").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("clean", clean),
                    ("portfolio_method", portfolio_method),
                    (
                        "weights",
                        weights if weights is None else ro.vectors.FloatVector(weights),
                    ),
                    ("mu", mu if mu is None else ro.vectors.FloatVector(mu)),
                    (
                        "sigma",
                        sigma if sigma is None else ro.vectors.FloatVector(sigma),
                    ),
                    ("use", use),
                    ("method", method),
                    ("SE", SE),
                ),
                lc,
            ),
            lc,
        )
