"""The PerformanceAnalytics M4.ewma function."""
from typing import Optional

import numpy as np
import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri, numpy2ri

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df


def ewma(R: pd.DataFrame, lambda_: float = 0.97, last_m3: Optional[np.ndarray] = None, as_mat: bool = True) -> np.ndarray:
    """Calculate M4.ewma."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + numpy2ri.converter + pandas2ri.converter).context():
            return np.array(robjects.r("M4.ewma").rcall(
                (
                    ("R", xts_from_df(R)),
                    ("lambda", lambda_),
                    ("last.M4", last_m3),
                    ("as.mat", as_mat),
                ),
                lc,
            ))
