"""The Performance Analytics chart.RollingPerformance function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df
from ..plot_img import plot_to_image


def rolling_performance(R: pd.DataFrame, width: int = 12, fun: Optional[str] = None, ylim: Optional[float] = None, main: Optional[str] = None):
    """Calculate chart.RollingPerformance."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if fun is None:
        fun = "Return.annualized"
    with robjects.local_context() as lc:
        return plot_to_image(lambda: robjects.r("plot").rcall(
            (
                ("x", robjects.r("chart.RollingPerformance").rcall(
                    (
                        ("R", xts_from_df(R)),
                        ("width", width),
                        ("FUN", fun),
                        ("ylim", ylim),
                        ("main", main),
                    ),
                    lc,
                )),
            ),
            lc,
        ))
