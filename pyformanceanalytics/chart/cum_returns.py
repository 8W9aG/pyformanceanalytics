"""The Performance Analytics chart.CumReturns function."""
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.cum_returns import CumReturns as RCumReturns


def CumReturns(
    R: pd.DataFrame,
    wealth_index: bool = False,
    geometric: bool = True,
    legend_loc: (str | None) = None,
    begin: (list[str] | None) = None,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.CumReturns."""
    if backend == Backend.R:
        return RCumReturns(
            R,
            wealth_index=wealth_index,
            geometric=geometric,
            legend_loc=legend_loc,
            begin=begin,
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for chart.CumReturns"
    )
