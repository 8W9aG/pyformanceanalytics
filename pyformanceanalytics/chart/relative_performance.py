"""The Performance Analytics chart.RelativePerformance function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.relative_performance import \
    RelativePerformance as RRelativePerformance


def RelativePerformance(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    main: (str | None) = None,
    xaxis: bool = True,
    colorset: (list[int] | None) = None,
    legend_loc: (str | None) = None,
    ylog: bool = False,
    element_color: (str | None) = None,
    lty: int = 1,
    cex_legend: float = 0.7,
    plot_width: int = 512,
    plot_height: int = 512,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.RelativePerformance."""
    if backend == Backend.R:
        return RRelativePerformance(
            Ra,
            Rb,
            plot_width,
            plot_height,
            main=main,
            xaxis=xaxis,
            colorset=colorset,
            legend_loc=legend_loc,
            ylog=ylog,
            element_color=element_color,
            lty=lty,
            cex_legend=cex_legend,
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for chart.RelativePerformance"
    )
