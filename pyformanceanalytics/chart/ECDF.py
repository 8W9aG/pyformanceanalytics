"""The Performance Analytics chart.ECDF function."""
from typing import Optional, List

import pandas as pd
from rpy2 import robjects
from rpy2.robjects.vectors import StrVector, IntVector

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df
from ..plot_img import plot_to_image


def ECDF(R: pd.DataFrame, main: Optional[str] = None, xlab: Optional[str] = None, ylab: Optional[str] = None, colorset: Optional[List[str]] = None, lwd: int = 1, lty: Optional[List[int]] = None, element_color: Optional[str] = None, xaxis: bool = True, yaxis: bool = True):
    """Calculate chart.ECDF."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if main is None:
        main = "Empirical CDF"
    if xlab is None:
        xlab = "x"
    if ylab is None:
        ylab = "F(x)"
    if colorset is None:
        colorset = ["black", "#005AFF"]
    if lty is None:
        lty = [1, 2]
    if element_color is None:
        element_color = "darkgray"
    with robjects.local_context() as lc:
        return plot_to_image(lambda: robjects.r("chart.ECDF").rcall(
            (
                ("R", xts_from_df(R)),
                ("main", main),
                ("xlab", xlab),
                ("ylab", ylab),
                ("colorset", StrVector(colorset)),
                ("lwd", lwd),
                ("lty", IntVector(lty)),
                ("element.color", element_color),
                ("xaxis", xaxis),
                ("yaxis", yaxis),
            ),
            lc,
        ))
