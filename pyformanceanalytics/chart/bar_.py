"""The Performance Analytics chart.Bar function."""
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.bar_ import Bar as RBar


def Bar(
    R: pd.DataFrame, legend_loc: (str | None) = None, backend: Backend = Backend.R
) -> Image.Image:
    """Calculate chart.Bar."""
    if backend == Backend.R:
        return RBar(R, legend_loc=legend_loc)
    raise NotImplementedError(f"Backend {backend.value} not implemented for chart.Bar")
