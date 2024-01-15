"""The Performance Analytics chart.RelativePerformance function."""
from typing import Optional, List

import pandas as pd
from rpy2 import robjects
from rpy2.robjects.vectors import StrVector, IntVector

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df
from ..plot_img import plot_to_image


def relative_performance(
        Ra: pd.DataFrame,
        Rb: pd.DataFrame,
        main: Optional[str] = None,
        xaxis: bool = True,
        colorset: Optional[List[int]] = None,
        legend_loc: Optional[str] = None,
        ylog: bool = False,
        element_color: Optional[str] = None,
        lty: int = 1,
        cex_legend: float = 0.7):
    """Calculate chart.RelativePerformance."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if main is None:
        main = "Relative Performance"
    if colorset is None:
        colorset = list(range(1, 12))
    if element_color is None:
        element_color = "darkgrey"
    with robjects.local_context() as lc:
        return plot_to_image(lambda: robjects.r("plot").rcall(
            (
                ("x", robjects.r("chart.RelativePerformance").rcall(
                    (
                        ("Ra", xts_from_df(Ra)),
                        ("Rb", xts_from_df(Rb)),
                        ("main", main),
                        ("xaxis", xaxis),
                        ("colorset", IntVector(colorset)),
                        ("legend.loc", legend_loc),
                        ("ylog", ylog),
                        ("element.color", element_color),
                        ("lty", lty),
                        ("cex.legend", cex_legend),
                    ),
                    lc,
                )),
            ),
            lc,
        ))
