"""The PerformanceAnalytics Omega function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame_or_float
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def Omega(
    R: pd.DataFrame,
    L: float = 0.0,
    method: (str | None) = None,
    output: (str | None) = None,
    Rf: (pd.DataFrame | None) = None,
    SE: bool = False,
) -> pd.DataFrame | float:
    """Calculate Omega."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if method is None:
        method = "simple"
    if output is None:
        output = "point"
    with ro.local_context() as lc:
        return as_data_frame_or_float(
            ro.r("Omega").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("L", L),
                    ("method", method),
                    ("output", output),
                    ("Rf", 0 if Rf is None else xts_from_df(Rf)),
                    ("SE", SE),
                ),
                lc,
            ),
            lc,
        )
