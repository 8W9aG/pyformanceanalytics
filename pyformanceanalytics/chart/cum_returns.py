"""The Performance Analytics chart.CumReturns function."""
from typing import Optional, List

import pandas as pd
from rpy2 import robjects
from rpy2.robjects.vectors import StrVector

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df
from ..plot_img import plot_to_image


def cum_returns(R: pd.DataFrame, wealth_index: bool = False, geometric: bool = True, legend_loc: Optional[str] = None, begin: Optional[List[str]] = None):
    """Calculate chart.CumReturns."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if begin is None:
        begin = ["first", "axis"]
    with robjects.local_context() as lc:
        return plot_to_image(lambda: robjects.r("plot").rcall(
            (
                ("x", robjects.r("chart.CumReturns").rcall(
                    (
                        ("R", xts_from_df(R)),
                        ("wealth.index", wealth_index),
                        ("geometric", geometric),
                        ("legend.loc", legend_loc),
                        ("begin", StrVector(begin)),
                    ),
                    lc,
                )),
            ),
            lc,
        ))
