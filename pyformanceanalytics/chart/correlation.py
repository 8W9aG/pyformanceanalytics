"""The Performance Analytics chart.Correlation function."""
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.correlation import Correlation as RCorrelation
from .correlation_method import CorrelationMethod


def Correlation(
    R: pd.DataFrame,
    histogram: bool = True,
    method: (str | CorrelationMethod | None) = None,
    plot_width: int = 512,
    plot_height: int = 512,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.Correlation."""
    if method is None:
        method = CorrelationMethod.PEARSON
    if backend == Backend.R:
        if isinstance(method, CorrelationMethod):
            method = method.value
        return RCorrelation(R, method, plot_width, plot_height, histogram=histogram)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for chart.Correlation"
    )
