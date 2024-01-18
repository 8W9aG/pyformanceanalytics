"""The PerformanceAnalytics sortDrawdowns function."""
import pandas as pd

from .backend.backend import Backend
from .backend.python.sort_drawdowns import sortDrawdowns as PYTHONsortDrawdowns


def sortDrawdowns(
    runs: pd.DataFrame, backend: Backend = Backend.PYTHON
) -> pd.DataFrame:
    """Calculate sortDrawdowns."""
    if backend == Backend.PYTHON:
        return PYTHONsortDrawdowns(runs)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for sortDrawdowns"
    )
