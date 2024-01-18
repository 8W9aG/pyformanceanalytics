"""The Performance Analytics chart.RollingPerformance function."""
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.rolling_performance import \
    RollingPerformance as RRollingPerformance


def RollingPerformance(
    R: pd.DataFrame,
    width: int = 12,
    fun: (str | None) = None,
    ylim: (float | None) = None,
    main: (str | None) = None,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.RollingPerformance."""
    if backend == Backend.R:
        return RRollingPerformance(R, width=width, fun=fun, ylim=ylim, main=main)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for chart.RollingPerformance"
    )
