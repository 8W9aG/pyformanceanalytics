"""The PerformanceAnalytics RPESE.control function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.RPESE.control import control as Rcontrol
from .control_estimator import ControlEstimator


def control(
    estimator: (str | ControlEstimator),
    se_method: (str | None) = None,
    clean_outliers: (bool | None) = None,
    fitting_method: (str | None) = None,
    freq_include: (str | None) = None,
    freq_par: (float | None) = None,
    a: (float | None) = None,
    b: (float | None) = None,
    backend: Backend = Backend.R,
) -> pd.DataFrame:
    """Calculate RPESE.control."""
    if backend == Backend.R:
        if isinstance(estimator, ControlEstimator):
            estimator = estimator.value
        return Rcontrol(
            estimator,
            se_method=se_method,
            clean_outliers=clean_outliers,
            fitting_method=fitting_method,
            freq_include=freq_include,
            freq_par=freq_par,
            a=a,
            b=b,
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for RPESE.control"
    )
