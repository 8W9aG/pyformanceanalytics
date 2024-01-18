"""The Performance Analytics chart.RollingMean function."""
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.rolling_mean import RollingMean as RRollingMean


def RollingMean(
    R: pd.DataFrame,
    width: int = 12,
    xaxis: bool = True,
    ylim: (float | None) = None,
    lwd: (list[int] | None) = None,
    plot_width: int = 512,
    plot_height: int = 512,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.RollingMean."""
    if backend == Backend.R:
        return RRollingMean(
            R, plot_width, plot_height, width=width, xaxis=xaxis, ylim=ylim, lwd=lwd
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for chart.RollingMean"
    )
