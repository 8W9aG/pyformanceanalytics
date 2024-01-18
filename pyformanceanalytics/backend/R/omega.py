"""The PerformanceAnalytics Omega function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from .r_df import as_data_frame
from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def Omega(
    R: pd.DataFrame,
    method: str,
    output: str,
    L: float = 0.0,
    Rf: (pd.DataFrame | None) = None,
    SE: bool = False,
) -> pd.DataFrame:
    """Calculate Omega."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
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
