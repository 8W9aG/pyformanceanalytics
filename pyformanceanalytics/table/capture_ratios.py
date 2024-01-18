"""The PerformanceAnalytics table.CaptureRatios function."""
import pandas as pd

from ..backend.backend import Backend
from ..backend.R.table.capture_ratios import CaptureRatios as RCaptureRatios


def CaptureRatios(
    Ra: pd.DataFrame, Rb: pd.DataFrame, digits: int = 4, backend: Backend = Backend.R
) -> pd.DataFrame:
    """Calculate table.CaptureRatios."""
    if backend == Backend.R:
        return RCaptureRatios(Ra, Rb, digits=digits)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for table.CaptureRatios"
    )
