"""The Performance Analytics chart.Correlation function."""
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.correlation import Correlation as RCorrelation


def Correlation(
    R: pd.DataFrame,
    histogram: bool = True,
    method: (list[str] | None) = None,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.Correlation."""
    if backend == Backend.R:
        return RCorrelation(R, histogram=histogram, method=method)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for chart.Correlation"
    )
