"""The Performance Analytics chart.ECDF function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.ECDF import ECDF as RECDF


def ECDF(
    R: pd.DataFrame,
    main: (str | None) = None,
    xlab: (str | None) = None,
    ylab: (str | None) = None,
    colorset: (list[str] | None) = None,
    lwd: int = 1,
    lty: (list[int] | None) = None,
    element_color: (str | None) = None,
    xaxis: bool = True,
    yaxis: bool = True,
    plot_width: int = 512,
    plot_height: int = 512,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.ECDF."""
    if backend == Backend.R:
        return RECDF(
            R,
            plot_width,
            plot_height,
            main=main,
            xlab=xlab,
            ylab=ylab,
            colorset=colorset,
            lwd=lwd,
            lty=lty,
            element_color=element_color,
            xaxis=xaxis,
            yaxis=yaxis,
        )
    raise NotImplementedError(f"Backend {backend.value} not implemented for chart.ECDF")
