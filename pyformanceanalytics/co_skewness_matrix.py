"""The PerformanceAnalytics CoSkewnessMatrix function."""
import numpy as np
import pandas as pd
from rpy2 import robjects

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def co_skewness_matrix(R: pd.DataFrame) -> np.ndarray:
    """Calculate CoSkewnessMatrix."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        return np.array(robjects.r("CoSkewnessMatrix").rcall(
            (
                ("R", xts_from_df(R)),
            ),
            lc,
        ))
