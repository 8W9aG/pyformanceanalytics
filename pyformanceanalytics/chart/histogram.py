"""The Performance Analytics chart.Histogram function."""
# pylint: disable=too-many-locals
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.histogram import Histogram as RHistogram


def Histogram(
    R: pd.DataFrame,
    breaks: (str | None) = None,
    main: (str | None) = None,
    xlab: (str | None) = None,
    ylab: (str | None) = None,
    methods: (list[str] | None) = None,
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
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.Histogram."""
    if backend == Backend.R:
        return RHistogram(
            R,
            breaks=breaks,
            main=main,
            xlab=xlab,
            ylab=ylab,
            methods=methods,
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
