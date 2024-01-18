"""The PerformanceAnalytics mean.LCL function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.mean.LCL import LCL as RLCL


def LCL(x: pd.DataFrame, backend: Backend = Backend.R) -> pd.DataFrame:
    """Calculate mean.LCL."""
    if backend == Backend.R:
        return RLCL(x)
    raise NotImplementedError(f"Backend {backend.value} not implemented for mean.LCL")
