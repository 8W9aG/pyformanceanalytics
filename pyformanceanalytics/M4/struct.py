"""The PerformanceAnalytics M4.struct function."""
from __future__ import annotations

import numpy as np
import pandas as pd

from ..backend.backend import Backend
from ..backend.R.M4.struct import struct as Rstruct
from .struct_type import StructType


def struct(
    R: pd.DataFrame,
    struct_type: (str | StructType | None) = None,
    f: (pd.DataFrame | None) = None,
    as_mat: bool = True,
    backend: Backend = Backend.R,
) -> np.ndarray:
    """Calculate M4.struct."""
    if struct_type is None:
        struct_type = StructType.INDEP
    if backend == Backend.R:
        if isinstance(struct_type, StructType):
            struct_type = struct_type.value
        return Rstruct(R, struct_type, f=f, as_mat=as_mat)
    raise NotImplementedError(f"Backend {backend.value} not implemented for M4.struct")
