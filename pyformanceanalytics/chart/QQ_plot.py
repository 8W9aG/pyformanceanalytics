"""The Performance Analytics chart.QQPlot function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.QQ_plot import QQPlot as RQQPlot
from .qq_plot_line import QQPlotLine


def QQPlot(
    R: pd.DataFrame,
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
    line: (str | QQPlotLine | None) = None,
    element_color: (str | None) = None,
    cex_axis: float = 0.8,
    cex_legend: float = 0.8,
    cex_lab: int = 1,
    cex_main: int = 1,
    xaxis: bool = True,
    yaxis: bool = True,
    ylim: (float | None) = None,
    distribution_parameter: (str | None) = None,
    plot_width: int = 512,
    plot_height: int = 512,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.QQPlot."""
    if line is None:
        line = QQPlotLine.QUARTILES
    if backend == Backend.R:
        if isinstance(line, QQPlotLine):
            line = line.value
        return RQQPlot(
            R,
            line,
            plot_width,
            plot_height,
            distributrion=distributrion,
            ylab=ylab,
            xlab=xlab,
            main=main,
            envelope=envelope,
            labels=labels,
            col=col,
            lwd=lwd,
            pch=pch,
            cex=cex,
            element_color=element_color,
            cex_axis=cex_axis,
            cex_legend=cex_legend,
            cex_lab=cex_lab,
            cex_main=cex_main,
            xaxis=xaxis,
            yaxis=yaxis,
            ylim=ylim,
            distribution_parameter=distribution_parameter,
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for chart.QQPlot"
    )
