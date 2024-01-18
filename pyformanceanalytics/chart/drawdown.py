"""The Performance Analytics chart.Drawdown function."""
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.drawdown import Drawdown as RDrawdown


def Drawdown(
    R: pd.DataFrame,
    geometric: bool = True,
    legend_loc: (str | None) = None,
    plot_width: int = 512,
    plot_height: int = 512,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.Drawdown."""
    if backend == Backend.R:
        return RDrawdown(
            R, plot_width, plot_height, geometric=geometric, legend_loc=legend_loc
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for chart.Drawdown"
    )
