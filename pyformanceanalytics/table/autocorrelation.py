"""The PerformanceAnalytics table.Autocorrelation function."""
import pandas as pd

from ..backend.backend import Backend
from ..backend.R.table.autocorrelation import \
    Autocorrelation as RAutocorrelation


def Autocorrelation(
    R: pd.DataFrame, digits: int = 4, backend: Backend = Backend.R
) -> pd.DataFrame:
    """Calculate table.Autocorrelation."""
    if backend == Backend.R:
        return RAutocorrelation(R, digits=digits)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for table.Autocorrelation"
    )
