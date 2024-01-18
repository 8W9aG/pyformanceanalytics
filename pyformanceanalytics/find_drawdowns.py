"""The PerformanceAnalytics findDrawdowns function."""
import pandas as pd

from .backend.backend import Backend
from .backend.R.find_drawdowns import findDrawdowns as RfindDrawdowns


def findDrawdowns(
    R: pd.DataFrame, geometric: bool = True, backend: Backend = Backend.R
) -> pd.DataFrame:
    """Calculate findDrawdowns."""
    if backend == Backend.R:
        return RfindDrawdowns(R, geometric=geometric)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for findDrawdowns"
    )
