"""The PerformanceAnalytics M4.shrink function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.M4.shrink import shrink as Rshrink


def shrink(
    R: pd.DataFrame,
    targets: int = 1,
    f: (pd.DataFrame | None) = None,
    as_mat: bool = True,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate M4.shrink."""
    if backend == Backend.R:
        return Rshrink(R, targets=targets, f=f, as_mat=as_mat)
    raise NotImplementedError(f"Backend {backend.value} not implemented for M4.shrink")
