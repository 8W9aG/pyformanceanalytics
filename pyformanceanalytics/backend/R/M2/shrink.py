"""The PerformanceAnalytics M2.shrink function."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def shrink(
    R: pd.DataFrame, targets: int = 1, f: (pd.DataFrame | None) = None
) -> pd.DataFrame | float:
    """Calculate M2.shrink."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("M2.shrink").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("targets", targets),
                    ("f", f),
                ),
                lc,
            ),
            lc,
        )
