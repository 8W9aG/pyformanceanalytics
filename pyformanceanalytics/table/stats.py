"""The PerformanceAnalytics table.Stats function."""
import pandas as pd

from ..backend.backend import Backend
from ..backend.R.table.stats import Stats as RStats


def Stats(
    R: pd.DataFrame, ci: float = 0.95, digits: int = 4, backend: Backend = Backend.R
) -> pd.DataFrame:
    """Calculate table.Stats."""
    if backend == Backend.R:
        return RStats(R, ci=ci, digits=digits)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for table.Stats"
    )
