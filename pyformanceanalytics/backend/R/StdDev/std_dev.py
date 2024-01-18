"""The PerformanceAnalytics StdDev function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def StdDev(
    R: pd.DataFrame,
    clean: str,
    portfolio_method: str,
    method: str,
    weights: (list[float] | None) = None,
    mu: (list[float] | None) = None,
    sigma: (list[float] | None) = None,
    use: (str | None) = None,
    SE: bool = False,
) -> pd.DataFrame:
    """Calculate StdDev."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if use is None:
        use = "everything"
    with ro.local_context() as lc:
        return as_data_frame(
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
