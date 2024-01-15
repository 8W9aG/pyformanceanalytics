"""The function for handling performance summaries charts."""
from typing import List, Optional

import pandas as pd
from rpy2 import robjects
from rpy2.robjects.vectors import StrVector

from ..ggplot_img import ggplot_to_image
from ..rimports import ensure_packages_present, GGPLOT2_PACKAGE, GRIDEXTRA_PACKAGE, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df


def performance_summary(
        R: pd.DataFrame,
        Rf: Optional[pd.DataFrame] = None,
        main: Optional[str] = None,
        geometric: bool = True,
        methods: Optional[str] = None,
        width: int = 0,
        event_labels: Optional[bool] = None,
        ylog: bool = False,
        wealth_index: bool = False,
        gap: int = 12,
        begin: Optional[List[str]] = None,
        legend_loc: Optional[str] = None,
        p: float = 0.95):
    """Calculate charts.PerformanceSummary."""
    ensure_packages_present([GGPLOT2_PACKAGE, GRIDEXTRA_PACKAGE, PERFORMANCE_ANALYTICS_PACKAGE])
    if methods is None:
        methods = "none"
    if begin is None:
        begin = ["first", "axis"]
    if legend_loc is None:
        legend_loc = "topleft"
    with robjects.local_context() as lc:
        plt = robjects.r("charts.PerformanceSummary").rcall(
            (
                ("R", xts_from_df(R)),
                ("Rf", 0 if Rf is None else xts_from_df(Rf)),
                ("main", main),
                ("geometric", geometric),
                ("methods", methods),
                ("width", width),
                ("event.labels", event_labels),
                ("ylog", ylog),
                ("wealth.index", wealth_index),
                ("gap", gap),
                ("begin", StrVector(begin)),
                ("legend.loc", legend_loc),
                ("p", p),
                ("plot.engine", "ggplot2"),
            ),
            lc,
        )
        return ggplot_to_image(plt)
