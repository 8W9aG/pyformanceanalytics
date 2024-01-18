"""The PerformanceAnalytics mean.stderr function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.mean.stderr import stderr as Rstderr


def stderr(x: pd.DataFrame, backend: Backend = Backend.R) -> pd.DataFrame:
    """Calculate mean.stderr."""
    if backend == Backend.R:
        return Rstderr(x)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for mean.stderr"
    )
