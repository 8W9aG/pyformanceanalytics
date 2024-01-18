"""The Performance Analytics chart.RollingCorrelation function."""
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.rolling_correlation import \
    RollingCorrelation as RRollingCorrelation


def RollingCorrelation(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    width: int = 12,
    xaxis: bool = True,
    legend_loc: (str | None) = None,
    colorset: (list[int] | None) = None,
    plot_width: int = 512,
    plot_height: int = 512,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.RollingCorrelation."""
    if backend == Backend.R:
        return RRollingCorrelation(
            Ra,
            Rb,
            plot_width,
            plot_height,
            width=width,
            xaxis=xaxis,
            legend_loc=legend_loc,
            colorset=colorset,
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for chart.RollingCorrelation"
    )
