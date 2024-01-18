"""The PerformanceAnalytics UpDownRatios function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.up_down_ratios import UpDownRatios as RUpDownRatios
from .up_down_ratios_method import UpDownRatiosMethod
from .up_down_ratios_side import UpDownRatiosSide


def UpDownRatios(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    method: (str | UpDownRatiosMethod | None) = None,
    side: (str | UpDownRatiosSide | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate UpDownRatios."""
    if method is None:
        method = UpDownRatiosMethod.CAPTURE
    if side is None:
        side = UpDownRatiosSide.UP
    if backend == Backend.R:
        if isinstance(method, UpDownRatiosMethod):
            method = method.value
        if isinstance(side, UpDownRatiosSide):
            side = side.value
        return RUpDownRatios(Ra, Rb, method, side)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for UpDownRatios"
    )
