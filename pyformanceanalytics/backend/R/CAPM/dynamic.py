"""The PerformanceAnalytics CAPM dynamic function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame_or_float
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def dynamic(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    Z: pd.DataFrame,
    Rf: (pd.DataFrame | float),
    lags: int = 1,
) -> pd.DataFrame | float:
    """Calculate dynamic."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame_or_float(
            ro.r("CAPM.dynamic").rcall(  # type: ignore
                (
                    ("Ra", xts_from_df(Ra)),
                    ("Rb", xts_from_df(Rb)),
                    ("Z", xts_from_df(Z)),
                    ("Rf", xts_from_df(Rf) if isinstance(Rf, pd.DataFrame) else Rf),
                    ("lags", lags),
                ),
                lc,
            ),
            lc,
        )
