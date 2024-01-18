"""The Performance Analytics chart.StackedBar function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.stacked_bar import StackedBar as RStackedBar


def StackedBar(
    w: pd.DataFrame,
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
    plot_width: int = 512,
    plot_height: int = 512,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.StackedBar."""
    if backend == Backend.R:
        return RStackedBar(
            w,
            plot_width,
            plot_height,
            colorset=colorset,
            space=space,
            cex_axis=cex_axis,
            cex_legend=cex_legend,
            cex_lab=cex_lab,
            cex_labels=cex_labels,
            cex_main=cex_main,
            xaxis=xaxis,
            legend_loc=legend_loc,
            element_color=element_color,
            unstacked=unstacked,
            xlab=xlab,
            ylab=ylab,
            ylim=ylim,
            date_format=date_format,
            major_ticks=major_ticks,
            minor_ticks=minor_ticks,
            las=las,
            xaxis_labels=xaxis_labels,
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for chart.StackedBar"
    )
