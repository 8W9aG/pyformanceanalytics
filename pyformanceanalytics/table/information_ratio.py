"""The PerformanceAnalytics table.InformationRatio function."""
import pandas as pd

from ..backend.backend import Backend
from ..backend.R.table.information_ratio import \
    InformationRatio as RInformationRatio


def InformationRatio(
    R: pd.DataFrame, Rb: pd.DataFrame, digits: int = 4, backend: Backend = Backend.R
) -> pd.DataFrame:
    """Calculate table.InformationRatio."""
    if backend == Backend.R:
        return RInformationRatio(R, Rb, digits=digits)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for table.InformationRatio"
    )
