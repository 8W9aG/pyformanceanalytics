"""The Performance Analytics chart.Events function."""
from __future__ import annotations

import datetime

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.events import Events as REvents


def Events(
    R: pd.DataFrame,
    dates: list[datetime.date],
    prior: int = 12,
    post: int = 12,
    main: (str | None) = None,
    xlab: (str | None) = None,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.Events."""
    if backend == Backend.R:
        return REvents(R, dates=dates, prior=prior, post=post, main=main, xlab=xlab)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for chart.Events"
    )
