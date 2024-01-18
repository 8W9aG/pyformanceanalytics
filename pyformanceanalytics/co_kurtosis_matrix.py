"""The PerformanceAnalytics CoKurtosisMatrix function."""
import numpy as np
import pandas as pd

from .backend.backend import Backend
from .backend.R.co_kurtosis_matrix import CoKurtosisMatrix as RCoKurtosisMatrix


def CoKurtosisMatrix(R: pd.DataFrame, backend: Backend = Backend.R) -> np.ndarray:
    """Calculate CoKurtosisMatrix."""
    if backend == Backend.R:
        return RCoKurtosisMatrix(R)
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for CoKurtosisMatrix"
    )
