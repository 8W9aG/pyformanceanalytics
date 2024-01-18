"""The PerformanceAnalytics SemiSD function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.semi_SD import SemiSD as RSemiSD


def SemiSD(
    R: pd.DataFrame, SE: bool = False, backend: Backend = Backend.R
) -> pd.DataFrame:
    """Calculate SemiSD."""
    if backend == Backend.R:
        return RSemiSD(R, SE=SE)
    raise NotImplementedError(f"Backend {backend.value} not implemented for SemiSD")
