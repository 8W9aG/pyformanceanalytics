"""The PerformanceAnalytics M2.ewma function."""
from __future__ import annotations

import numpy as np
import pandas as pd
from rpy2 import robjects as ro

from ..r_df import as_data_frame
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def ewma(
    R: pd.DataFrame, lambda_: float = 0.97, last_m2: (np.ndarray | None) = None
) -> pd.DataFrame:
    """Calculate M2.ewma."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return as_data_frame(
            ro.r("M2.ewma").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("lambda", lambda_),
                    ("last.M2", last_m2),
                ),
                lc,
            ),
            lc,
        )
