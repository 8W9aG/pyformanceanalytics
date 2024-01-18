"""The PerformanceAnalytics table.Variability function."""
import pandas as pd

from ..backend.backend import Backend
from ..backend.R.table import variability


def Variability(
    R: pd.DataFrame,
    geometric: bool = True,
    digits: int = 4,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate table.Variability."""
    if backend == Backend.R:
        return variability.Variability(R, geometric=geometric, digits=digits)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for table.Variability"
    )
