"""The Performance Analytics chart.ACF function."""
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.ACF import ACF as RACF


def ACF(
    R: pd.DataFrame,
    maxlag: (int | None) = None,
    elementcolor: (str | None) = None,
    main: (str | None) = None,
    plot_width: int = 512,
    plot_height: int = 512,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.ACF."""
    if backend == Backend.R:
        return RACF(
            R,
            plot_width,
            plot_height,
            maxlag=maxlag,
            elementcolor=elementcolor,
            main=main,
        )
    raise NotImplementedError(f"Backend {backend.value} not implemented for chart.ACF")
