"""The Performance Analytics charts.RollingPerformance function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df
from ..plot_img import plot_to_image


def rolling_performance(R: pd.DataFrame, width: int = 12, Rf: Optional[pd.DataFrame] = None, main: Optional[str] = None, event_labels: Optional[bool] = None, legend_loc: Optional[str] = None):
    """Calculate charts.RollingPerformance."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        return plot_to_image(lambda: robjects.r("charts.RollingPerformance").rcall(
            (
                ("R", xts_from_df(R)),
                ("width", width),
                ("Rf", 0 if Rf is None else xts_from_df(Rf)),
                ("main", main),
                ("event.labels", event_labels),
                ("legend.loc", legend_loc),
            ),
            lc,
        ))
