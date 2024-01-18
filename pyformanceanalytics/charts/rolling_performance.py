"""The Performance Analytics charts.RollingPerformance function."""
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.charts.rolling_performance import \
    RollingPerformance as RRollingPerformance


def RollingPerformance(
    R: pd.DataFrame,
    width: int = 12,
    Rf: (pd.DataFrame | float) = 0.0,
    main: (str | None) = None,
    event_labels: (bool | None) = None,
    legend_loc: (str | None) = None,
    plot_width: int = 512,
    plot_height: int = 512,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate charts.RollingPerformance."""
    if backend == Backend.R:
        return RRollingPerformance(
            R,
            plot_width,
            plot_height,
            Rf,
            width=width,
            main=main,
            event_labels=event_labels,
            legend_loc=legend_loc,
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for charts.RollingPerformance"
    )
