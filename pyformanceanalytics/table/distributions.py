"""The PerformanceAnalytics table.Distributions function."""
import pandas as pd

from ..backend.backend import Backend
from ..backend.R.table.distributions import Distributions as RDistributions


def Distributions(
    R: pd.DataFrame, digits: int = 4, backend: Backend = Backend.R
) -> pd.DataFrame:
    """Calculate table.Distributions."""
    if backend == Backend.R:
        return RDistributions(R, digits=digits)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for table.Distributions"
    )
