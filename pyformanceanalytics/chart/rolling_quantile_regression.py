"""The Performance Analytics chart.RollingQuantileRegression function."""
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.rolling_quantile_regression import \
    RollingQuantileRegression as RRollingQuantileRegression
from .rolling_regression_attribute import RollingRegressionAttribute


def RollingQuantileRegression(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    width: int = 12,
    Rf: (pd.DataFrame | float) = 0.0,
    attribute: (str | RollingRegressionAttribute | None) = None,
    main: (str | None) = None,
    na_pad: bool = True,
    plot_width: int = 512,
    plot_height: int = 512,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.RollingQuantileRegression."""
    if attribute is None:
        attribute = RollingRegressionAttribute.BETA
    if backend == Backend.R:
        if isinstance(attribute, RollingRegressionAttribute):
            attribute = attribute.value
        return RRollingQuantileRegression(
            Ra,
            Rb,
            attribute,
            plot_width,
            plot_height,
            Rf,
            width=width,
            main=main,
            na_pad=na_pad,
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for chart.RollingQuantileRegression"
    )
