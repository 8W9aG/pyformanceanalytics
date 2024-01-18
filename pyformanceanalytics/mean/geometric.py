"""The PerformanceAnalytics mean.geometric function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.mean.geometric import geometric as Rgeometric


def geometric(x: pd.DataFrame, backend: Backend = Backend.R) -> pd.DataFrame:
    """Calculate mean.geometric."""
    if backend == Backend.R:
        return Rgeometric(x)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for mean.geometric"
    )
