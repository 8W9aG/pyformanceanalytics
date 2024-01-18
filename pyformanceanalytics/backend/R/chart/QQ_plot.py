"""The Performance Analytics chart.QQPlot function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image
from rpy2 import robjects as ro

from ..plot_img import plot_to_image
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def QQPlot(
    R: pd.DataFrame,
    line: str,
    plot_width: int,
    plot_height: int,
    distributrion: (str | None) = None,
    ylab: (str | None) = None,
    xlab: (str | None) = None,
    main: (str | None) = None,
    envelope: bool = False,
    labels: bool = False,
    col: (list[int] | None) = None,
    lwd: int = 2,
    pch: int = 1,
    cex: int = 1,
    element_color: (str | None) = None,
    cex_axis: float = 0.8,
    cex_legend: float = 0.8,
    cex_lab: int = 1,
    cex_main: int = 1,
    xaxis: bool = True,
    yaxis: bool = True,
    ylim: (float | None) = None,
    distribution_parameter: (str | None) = None,
) -> Image.Image:
    """Calculate chart.QQPlot."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if distributrion is None:
        distributrion = "norm"
    if xlab is None:
        xlab = f"{distributrion} Quantiles"
    if col is None:
        col = [1, 4]
    if element_color is None:
        element_color = "darkgray"
    with ro.local_context() as lc:
        return plot_to_image(
            lambda: ro.r("chart.QQPlot").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("distribution", distributrion),
                    ("ylab", ylab),
                    ("xlab", xlab),
                    ("main", main),
                    ("envelope", envelope),
                    ("labels", labels),
                    ("col", ro.vectors.IntVector(col)),
                    ("lwd", lwd),
                    ("pch", pch),
                    ("cex", cex),
                    ("line", ro.vectors.StrVector([line])),
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
            ),
            plot_width,
            plot_height,
        )
