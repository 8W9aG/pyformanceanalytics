"""The PerformanceAnalytics M3.struct function."""
from __future__ import annotations

import numpy as np
import pandas as pd

from ..backend.backend import Backend
from ..backend.R.M3.struct import struct as Rstruct
from .struct_type import StructType


def struct(
    R: pd.DataFrame,
    struct_type: (str | StructType | None) = None,
    f: (pd.DataFrame | None) = None,
    unbiased_marg: bool = False,
    as_mat: bool = True,
    backend: Backend = Backend.R,
) -> np.ndarray:
    """Calculate M3.struct."""
    if struct_type is None:
        struct_type = StructType.INDEP
    if backend == Backend.R:
        if isinstance(struct_type, StructType):
            struct_type = struct_type.value
        return Rstruct(R, struct_type, f=f, unbiased_marg=unbiased_marg, as_mat=as_mat)
    raise NotImplementedError(f"Backend {backend.value} not implemented for M3.struct")
