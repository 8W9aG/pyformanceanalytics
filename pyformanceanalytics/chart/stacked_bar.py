"""The Performance Analytics chart.StackedBar function."""
from typing import Optional, List

import pandas as pd
from rpy2 import robjects
from rpy2.robjects.vectors import StrVector

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df
from ..plot_img import plot_to_image


def stacked_bar(
        w: pd.DataFrame,
        colorset: Optional[int] = None,
        space: float = 0.2,
        cex_axis: float = 0.8,
        cex_legend: float = 0.8,
        cex_lab: int = 1,
        cex_labels: float = 0.8,
        cex_main: int = 1,
        xaxis: bool = True,
        legend_loc: Optional[str] = None,
        element_color: Optional[str] = None,
        unstacked: bool = True,
        xlab: Optional[str] = None,
        ylab: Optional[str] = None,
        ylim: Optional[float] = None,
        date_format: Optional[str] = None,
        major_ticks: Optional[str] = None,
        minor_ticks: bool = True,
        las: int = 0,
        xaxis_labels: Optional[List[str]] = None):
    """Calculate chart.StackedBar."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if legend_loc is None:
        legend_loc = "under"
    if element_color is None:
        element_color = "darkgray"
    if xlab is None:
        xlab = "Date"
    if ylab is None:
        ylab = "Value"
    if date_format is None:
        date_format = "%b %y"
    if major_ticks is None:
        major_ticks = "auto"
    with robjects.local_context() as lc:
        return plot_to_image(lambda: robjects.r("chart.StackedBar").rcall(
            (
                ("w", xts_from_df(w)),
                ("colorset", colorset),
                ("space", space),
                ("cex.axis", cex_axis),
                ("cex.legend", cex_legend),
                ("cex.lab", cex_lab),
                ("cex.labels", cex_labels),
                ("cex.main", cex_main),
                ("xaxis", xaxis),
                ("legend.loc", legend_loc),
                ("element.color", element_color),
                ("unstacked", unstacked),
                ("xlab", xlab),
                ("ylab", ylab),
                ("ylim", ylim),
                ("date_format", date_format),
                ("major_ticks", major_ticks),
                ("minor_ticks", minor_ticks),
                ("las", las),
                ("xaxis_labels", None if xaxis_labels is None else StrVector(xaxis_labels)),
            ),
            lc,
        ))
