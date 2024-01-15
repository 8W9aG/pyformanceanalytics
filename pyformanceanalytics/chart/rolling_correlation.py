"""The Performance Analytics chart.RollingCorrelation function."""
from typing import Optional, List

import pandas as pd
from rpy2 import robjects
from rpy2.robjects.vectors import IntVector

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df
from ..plot_img import plot_to_image


def rolling_correlation(Ra: pd.DataFrame, Rb: pd.DataFrame, width: int = 12, xaxis: bool = True, legend_loc: Optional[str] = None, colorset: Optional[List[int]] = None):
    """Calculate chart.RollingCorrelation."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if colorset is None:
        colorset = list(range(1, 12))
    with robjects.local_context() as lc:
        return plot_to_image(lambda: robjects.r("plot").rcall(
            (
                ("x", robjects.r("chart.RollingCorrelation").rcall(
                    (
                        ("Ra", xts_from_df(Ra)),
                        ("Rb", xts_from_df(Rb)),
                        ("width", width),
                        ("xaxis", xaxis),
                        ("legend.loc", legend_loc),
                        ("colorset", IntVector(colorset))
                    ),
                    lc,
                )),
            ),
            lc,
        ))
