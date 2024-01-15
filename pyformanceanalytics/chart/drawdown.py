"""The Performance Analytics chart.Drawdown function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects
from rpy2.robjects.vectors import StrVector

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df
from ..plot_img import plot_to_image


def drawdown(R: pd.DataFrame, geometric: bool = True, legend_loc: Optional[str] = None):
    """Calculate chart.Drawdown."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        return plot_to_image(lambda: robjects.r("plot").rcall(
            (
                ("x", robjects.r("chart.Drawdown").rcall(
                    (
                        ("R", xts_from_df(R)),
                        ("geometric", geometric),
                        ("legend.loc", legend_loc),
                    ),
                    lc,
                )),
            ),
            lc,
        ))
