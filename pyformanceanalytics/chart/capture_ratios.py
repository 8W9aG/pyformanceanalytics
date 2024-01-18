"""The Performance Analytics chart.CaptureRatios function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.capture_ratios import CaptureRatios as RCaptureRatios


def CaptureRatios(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    main: (str | None) = None,
    add_names: bool = True,
    xlab: (str | None) = None,
    ylab: (str | None) = None,
    colorset: int = 1,
    symbolset: int = 1,
    legend_loc: (str | None) = None,
    xlim: (float | None) = None,
    ylim: (float | None) = None,
    cex_legend: int = 1,
    cex_axis: float = 0.8,
    cex_main: int = 1,
    cex_lab: int = 1,
    element_color: (str | None) = None,
    benchmark_color: (str | None) = None,
    plot_width: int = 512,
    plot_height: int = 512,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.CaptureRatios."""
    if backend == Backend.R:
        return RCaptureRatios(
            Ra,
            Rb,
            plot_width,
            plot_height,
            main=main,
            add_names=add_names,
            xlab=xlab,
            ylab=ylab,
            colorset=colorset,
            symbolset=symbolset,
            legend_loc=legend_loc,
            xlim=xlim,
            ylim=ylim,
            cex_legend=cex_legend,
            cex_axis=cex_axis,
            cex_main=cex_main,
            cex_lab=cex_lab,
            element_color=element_color,
            benchmark_color=benchmark_color,
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for chart.CaptureRatios"
    )
