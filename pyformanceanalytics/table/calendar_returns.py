"""The PerformanceAnalytics table.CalendarReturns function."""
import pandas as pd

from ..backend.backend import Backend
from ..backend.R.table.calendar_returns import \
    CalendarReturns as RCalendarReturns


def CalendarReturns(
    R: pd.DataFrame,
    digits: int = 1,
    as_perc: bool = True,
    geometric: bool = True,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate table.CalendarReturns."""
    if backend == Backend.R:
        return RCalendarReturns(R, digits=digits, as_perc=as_perc, geometric=geometric)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for table.CalendarReturns"
    )
