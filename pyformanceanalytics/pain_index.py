"""The PerformanceAnalytics PainIndex function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.pain_index import PainIndex as RPainIndex


def PainIndex(R: pd.DataFrame, backend: Backend = Backend.R) -> pd.DataFrame:
    """Calculate PainIndex."""
    if backend == Backend.R:
        return RPainIndex(R)
    raise NotImplementedError(f"Backend {backend.value} not implemented for PainIndex")
