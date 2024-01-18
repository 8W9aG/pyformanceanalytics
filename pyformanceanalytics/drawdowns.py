"""The PerformanceAnalytics Drawdowns function."""
import pandas as pd

from .backend.backend import Backend
from .backend.R.drawdowns import Drawdowns as RDrawdowns


def Drawdowns(
    R: pd.DataFrame, geometric: bool = True, backend: Backend = Backend.R
) -> pd.DataFrame:
    """Calculate Drawdowns."""
    if backend == Backend.R:
        return RDrawdowns(R, geometric=geometric)
    raise NotImplementedError(f"Backend {backend.value} not implemented for Drawdowns")
