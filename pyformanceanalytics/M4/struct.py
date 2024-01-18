"""The PerformanceAnalytics M4.struct function."""
from __future__ import annotations

import numpy as np
import pandas as pd

from ..backend.backend import Backend
from ..backend.R.M4.struct import struct as Rstruct


def struct(
    R: pd.DataFrame,
    struct_type: (str | None) = None,
    f: (pd.DataFrame | None) = None,
    as_mat: bool = True,
    backend: Backend = Backend.R,
) -> np.ndarray:
    """Calculate M4.struct."""
    if backend == Backend.R:
        return Rstruct(R, struct_type=struct_type, f=f, as_mat=as_mat)
    raise NotImplementedError(f"Backend {backend.value} not implemented for M4.struct")
