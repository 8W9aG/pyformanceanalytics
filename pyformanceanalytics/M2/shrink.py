"""The PerformanceAnalytics M2.shrink function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.M2.shrink import shrink as Rshrink


def shrink(
    R: pd.DataFrame,
    targets: int = 1,
    f: (pd.DataFrame | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate M2.shrink."""
    if backend == Backend.R:
        return Rshrink(R, targets=targets, f=f)
    raise NotImplementedError(f"Backend {backend.value} not implemented for M2.shrink")
