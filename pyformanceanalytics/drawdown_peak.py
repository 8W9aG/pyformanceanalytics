"""The PerformanceAnalytics DrawdownPeak function."""
from __future__ import annotations

import numpy as np
import pandas as pd

from .backend.backend import Backend
from .backend.R.drawdown_peak import DrawdownPeak as RDrawdownPeak


def DrawdownPeak(R: pd.DataFrame, backend: Backend = Backend.R) -> np.ndarray:
    """Calculate DrawdownPeak."""
    if backend == Backend.R:
        return RDrawdownPeak(R)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for DrawdownPeak"
    )
