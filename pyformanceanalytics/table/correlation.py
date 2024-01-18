"""The PerformanceAnalytics table.Correlation function."""
import pandas as pd

from ..backend.backend import Backend
from ..backend.R.table.correlation import Correlation as RCorrelation


def Correlation(
    Ra: pd.DataFrame, Rb: pd.DataFrame, backend: Backend = Backend.R
) -> pd.DataFrame:
    """Calculate table.Correlation."""
    if backend == Backend.R:
        return RCorrelation(Ra, Rb)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for table.Correlation"
    )
