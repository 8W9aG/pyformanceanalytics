"""The PerformanceAnalytics table.Drawdowns function."""
import pandas as pd

from ..backend.backend import Backend
from ..backend.R.table.drawdowns import Drawdowns as RDrawdowns


def Drawdowns(
    R: pd.DataFrame,
    top: int = 5,
    digits: int = 4,
    geometric: bool = True,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate table.Drawdowns."""
    if backend == Backend.R:
        return RDrawdowns(R, top=top, digits=digits, geometric=geometric)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for table.Drawdowns"
    )
