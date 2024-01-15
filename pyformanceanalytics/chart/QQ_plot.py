"""The Performance Analytics chart.QQPlot function."""
from typing import Optional, List

import pandas as pd
from rpy2 import robjects
from rpy2.robjects.vectors import StrVector, IntVector

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df
from ..plot_img import plot_to_image


def QQ_plot(
        R: pd.DataFrame,
        distributrion: Optional[str] = None,
        ylab: Optional[str] = None,
        xlab: Optional[str] = None,
        main: Optional[str] = None,
        envelope: bool = False,
        labels: bool = False,
        col: Optional[List[int]] = None,
        lwd: int = 2,
        pch: int = 1,
        cex: int = 1,
        line: Optional[List[str]] = None,
        element_color: Optional[str] = None,
        cex_axis: float = 0.8,
        cex_legend: float = 0.8,
        cex_lab: int = 1,
        cex_main: int = 1,
        xaxis: bool = True,
        yaxis: bool = True,
        ylim: Optional[float] = None,
        distribution_parameter: Optional[str] = None):
    """Calculate chart.QQPlot."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if distributrion is None:
        distributrion = "norm"
    if xlab is None:
        xlab = f"{distributrion} Quantiles"
    if col is None:
        col = [1, 4]
    if line is None:
        line = ["quartiles", "robust", "none"]
    if element_color is None:
        element_color = "darkgray"
    with robjects.local_context() as lc:
        return plot_to_image(lambda: robjects.r("chart.QQPlot").rcall(
            (
                ("R", xts_from_df(R)),
                ("distribution", distributrion),
                ("ylab", ylab),
                ("xlab", xlab),
                ("main", main),
                ("envelope", envelope),
                ("labels", labels),
                ("col", IntVector(col)),
                ("lwd", lwd),
                ("pch", pch),
                ("cex", cex),
                ("line", StrVector(line)),
                ("element.color", element_color),
                ("cex.axis", cex_axis),
                ("cex.legend", cex_legend),
                ("cex.lab", cex_lab),
                ("cex.main", cex_main),
                ("xaxis", xaxis),
                ("yaxis", yaxis),
                ("ylim", ylim),
                ("distributionParameter", distribution_parameter),
            ),
            lc,
        ))
