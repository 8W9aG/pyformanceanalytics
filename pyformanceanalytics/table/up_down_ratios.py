"""The PerformanceAnalytics table.UpDownRatios function."""
import pandas as pd

from ..backend.backend import Backend
from ..backend.R.table.up_down_ratios import UpDownRatios as RUpDownRatios


def UpDownRatios(
    Ra: pd.DataFrame, Rb: pd.DataFrame, digits: int = 4, backend: Backend = Backend.R
) -> pd.DataFrame:
    """Calculate table.UpDownRatios."""
    if backend == Backend.R:
        return RUpDownRatios(Ra, Rb, digits=digits)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for table.UpDownRatios"
    )
