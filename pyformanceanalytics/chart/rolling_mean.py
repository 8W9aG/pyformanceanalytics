"""The Performance Analytics chart.RollingMean function."""
from typing import Optional, List

import pandas as pd
from rpy2 import robjects
from rpy2.robjects.vectors import IntVector

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df
from ..plot_img import plot_to_image


def rolling_mean(R: pd.DataFrame, width: int = 12, xaxis: bool = True, ylim: Optional[float] = None, lwd: Optional[List[int]] = None):
    """Calculate chart.RollingMean."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if lwd is None:
        lwd = [2, 1, 1]
    with robjects.local_context() as lc:
        return plot_to_image(lambda: robjects.r("plot").rcall(
            (
                ("x", robjects.r("chart.RollingMean").rcall(
                    (
                        ("R", xts_from_df(R)),
                        ("width", width),
                        ("xaxis", xaxis),
                        ("ylim", ylim),
                        ("lwd", IntVector(lwd)),
                    ),
                    lc,
                )),
            ),
            lc,
        ))
