"""The PerformanceAnalytics CoSkewnessMatrix function."""
import numpy as np
import pandas as pd

from .backend.backend import Backend
from .backend.R.co_skewness_matrix import CoSkewnessMatrix as RCoSkewnessMatrix


def CoSkewnessMatrix(R: pd.DataFrame, backend: Backend = Backend.R) -> np.ndarray:
    """Calculate CoSkewnessMatrix."""
    if backend == Backend.R:
        return RCoSkewnessMatrix(R)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for CoSkewnessMatrix"
    )
