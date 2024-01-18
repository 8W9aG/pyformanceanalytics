"""The PerformanceAnalytics M3.ewma function."""
from __future__ import annotations

import numpy as np
import pandas as pd
from rpy2 import robjects as ro
from rpy2.robjects import numpy2ri

from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def ewma(
    R: pd.DataFrame,
    lambda_: float = 0.97,
    last_m3: (np.ndarray | None) = None,
    as_mat: bool = True,
) -> np.ndarray:
    """Calculate M3.ewma."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        with (ro.default_converter + numpy2ri.converter).context():
            return np.array(
                ro.r("M3.ewma").rcall(  # type: ignore
                    (
                        ("R", xts_from_df(R)),
                        ("lambda", lambda_),
                        ("last.M3", last_m3),
                        ("as.mat", as_mat),
                    ),
                    lc,
                )
            )
