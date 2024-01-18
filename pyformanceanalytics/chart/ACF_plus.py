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
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.ACFplus."""
    if backend == Backend.R:
        return RACFplus(R, maxlag=maxlag, elementcolor=elementcolor, main=main)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for chart.ACFplus"
    )
