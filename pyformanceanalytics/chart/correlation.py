"""The Performance Analytics chart.Correlation function."""
from typing import Optional, List

import pandas as pd
from rpy2 import robjects
from rpy2.robjects.vectors import StrVector

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df
from ..plot_img import plot_to_image


def correlation(R: pd.DataFrame, histogram: bool = True, method: Optional[List[str]] = None):
    """Calculate chart.CaptureRatios."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if method is None:
        method = ["pearson", "kendall", "spearman"]
    with robjects.local_context() as lc:
        return plot_to_image(lambda: robjects.r("chart.Correlation").rcall(
            (
                ("R", xts_from_df(R)),
                ("histogram", histogram),
                ("method", StrVector(method)),
            ),
            lc,
        ))
