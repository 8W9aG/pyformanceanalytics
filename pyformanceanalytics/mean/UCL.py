"""The PerformanceAnalytics mean.UCL function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.mean.UCL import UCL as RUCL


def UCL(x: pd.DataFrame, backend: Backend = Backend.R) -> pd.DataFrame | float:
    """Calculate mean.UCL."""
    if backend == Backend.R:
        return RUCL(x)
    raise NotImplementedError(f"Backend {backend.value} not implemented for mean.UCL")
