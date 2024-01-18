"""The Performance Analytics chart.ACFplus function."""
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.ACF_plus import ACFplus as RACFplus


def ACFplus(
    R: pd.DataFrame,
    maxlag: (int | None) = None,
    elementcolor: (str | None) = None,
    main: (str | None) = None,
    plot_width: int = 512,
    plot_height: int = 512,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.ACFplus."""
    if backend == Backend.R:
        return RACFplus(
            R,
            plot_width,
            plot_height,
            maxlag=maxlag,
            elementcolor=elementcolor,
            main=main,
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for chart.ACFplus"
    )
