"""The Performance Analytics chart.StackedBar function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image
from rpy2 import robjects as ro

from ..plot_img import plot_to_image
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def StackedBar(
    w: pd.DataFrame,
    plot_width: int,
    plot_height: int,
    colorset: (int | None) = None,
    space: float = 0.2,
    cex_axis: float = 0.8,
    cex_legend: float = 0.8,
    cex_lab: int = 1,
    cex_labels: float = 0.8,
    cex_main: int = 1,
    xaxis: bool = True,
    legend_loc: (str | None) = None,
    element_color: (str | None) = None,
    unstacked: bool = True,
    xlab: (str | None) = None,
    ylab: (str | None) = None,
    ylim: (float | None) = None,
    date_format: (str | None) = None,
    major_ticks: (str | None) = None,
    minor_ticks: bool = True,
    las: int = 0,
    xaxis_labels: (list[str] | None) = None,
) -> Image.Image:
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
    with ro.local_context() as lc:
        return plot_to_image(
            lambda: ro.r("chart.StackedBar").rcall(  # type: ignore
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
                    (
                        "xaxis_labels",
                        None
                        if xaxis_labels is None
                        else ro.vectors.StrVector(xaxis_labels),
                    ),
                ),
                lc,
            ),
            plot_width,
            plot_height,
        )
