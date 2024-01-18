"""The Performance Analytics chart.RollingQuantileRegression function."""
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.rolling_quantile_regression import \
    RollingQuantileRegression as RRollingQuantileRegression


def RollingQuantileRegression(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    width: int = 12,
    Rf: (pd.DataFrame | None) = None,
    attribute: (list[str] | None) = None,
    main: (str | None) = None,
    na_pad: bool = True,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.RollingQuantileRegression."""
    if backend == Backend.R:
        return RRollingQuantileRegression(
            Ra, Rb, width=width, Rf=Rf, attribute=attribute, main=main, na_pad=na_pad
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for chart.RollingQuantileRegression"
    )
