"""The Performance Analytics chart.CumReturns function."""
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.cum_returns import CumReturns as RCumReturns
from .cum_returns_begin import CumReturnsBegin


def CumReturns(
    R: pd.DataFrame,
    wealth_index: bool = False,
    geometric: bool = True,
    legend_loc: (str | None) = None,
    begin: (str | CumReturnsBegin | None) = None,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.CumReturns."""
    if begin is None:
        begin = CumReturnsBegin.FIRST
    if backend == Backend.R:
        if isinstance(begin, CumReturnsBegin):
            begin = begin.value
        return RCumReturns(
            R,
            begin,
            wealth_index=wealth_index,
            geometric=geometric,
            legend_loc=legend_loc,
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for chart.CumReturns"
    )
