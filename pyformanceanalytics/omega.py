"""The PerformanceAnalytics Omega function."""
from __future__ import annotations

import pandas as pd

from .backend.backend import Backend
from .backend.R.omega import Omega as ROmega
from .omega_method import OmegaMethod
from .omega_output import OmegaOutput


def Omega(
    R: pd.DataFrame,
    L: float = 0.0,
    method: (str | OmegaMethod | None) = None,
    output: (str | OmegaOutput | None) = None,
    Rf: (pd.DataFrame | float) = 0.0,
    SE: bool = False,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate Omega."""
    if method is None:
        method = OmegaMethod.SIMPLE
    if output is None:
        output = OmegaOutput.POINT
    if backend == Backend.R:
        if isinstance(method, OmegaMethod):
            method = method.value
        if isinstance(output, OmegaOutput):
            output = output.value
        return ROmega(R, method, output, Rf, L=L, SE=SE)
    raise NotImplementedError(f"Backend {backend.value} not implemented for Omega")
