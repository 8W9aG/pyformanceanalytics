"""The PerformanceAnalytics M2.struct function."""
from __future__ import annotations

import numpy as np
import pandas as pd

from ..backend.backend import Backend
from ..backend.R.M2.struct import struct as Rstruct


def struct(
    R: pd.DataFrame,
    struct_type: (str | None) = None,
    f: (pd.DataFrame | None) = None,
    backend: Backend = Backend.R,
) -> np.ndarray:
    """Calculate M2.struct."""
    if backend == Backend.R:
        return Rstruct(R, struct_type=struct_type, f=f)
    raise NotImplementedError(f"Backend {backend.value} not implemented for M2.struct")
