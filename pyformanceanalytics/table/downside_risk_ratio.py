"""The PerformanceAnalytics table.DownsideRiskRatio function."""
import pandas as pd

from ..backend.backend import Backend
from ..backend.R.table.downside_risk_ratio import \
    DownsideRiskRatio as RDownsideRiskRatio


def DownsideRiskRatio(
    R: pd.DataFrame,
    MAR: float = 0.1 / 12.0,
    digits: int = 4,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate table.DownsideRiskRatio."""
    if backend == Backend.R:
        return RDownsideRiskRatio(R, MAR=MAR, digits=digits)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for table.DownsideRiskRatio"
    )
