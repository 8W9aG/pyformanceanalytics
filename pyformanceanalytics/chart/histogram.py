"""The Performance Analytics chart.Histogram function."""
# pylint: disable=too-many-locals
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.histogram import Histogram as RHistogram
from .histogram_methods import HistogramMethods


def Histogram(
    R: pd.DataFrame,
    breaks: (str | None) = None,
    main: (str | None) = None,
    xlab: (str | None) = None,
    ylab: (str | None) = None,
    methods: (list[str | HistogramMethods] | None) = None,
    show_outliers: bool = True,
    colorset: (list[str] | None) = None,
    border_col: (str | None) = None,
    lwd: int = 2,
    xlim: (float | None) = None,
    ylim: (float | None) = None,
    element_color: (str | None) = None,
    note_lines: (list[float] | None) = None,
    note_labels: (list[str] | None) = None,
    note_cex: float = 0.7,
    note_color: (str | None) = None,
    probability: bool = False,
    p: float = 0.95,
    cex_axis: float = 0.8,
    cex_legend: float = 0.8,
    cex_lab: int = 1,
    cex_main: int = 1,
    xaxis: bool = True,
    yaxis: bool = True,
    plot_width: int = 512,
    plot_height: int = 512,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.Histogram."""
    if methods is None:
        methods = [
            HistogramMethods.NONE,
            HistogramMethods.ADD_DENSITY,
            HistogramMethods.ADD_NORMAL,
            HistogramMethods.ADD_CENTERED,
            HistogramMethods.ADD_CAUCHY,
            HistogramMethods.ADD_SST,
            HistogramMethods.ADD_RUG,
            HistogramMethods.ADD_RISK,
            HistogramMethods.ADD_QQPLOT,
        ]
    if backend == Backend.R:
        return RHistogram(
            R,
            [x.value if isinstance(x, HistogramMethods) else x for x in methods],
            plot_width,
            plot_height,
            breaks=breaks,
            main=main,
            xlab=xlab,
            ylab=ylab,
            show_outliers=show_outliers,
            colorset=colorset,
            border_col=border_col,
            lwd=lwd,
            xlim=xlim,
            ylim=ylim,
            element_color=element_color,
            note_lines=note_lines,
            note_labels=note_labels,
            note_cex=note_cex,
            note_color=note_color,
            probability=probability,
            p=p,
            cex_axis=cex_axis,
            cex_legend=cex_legend,
            cex_lab=cex_lab,
            cex_main=cex_main,
            xaxis=xaxis,
            yaxis=yaxis,
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for chart.Histogram"
    )
