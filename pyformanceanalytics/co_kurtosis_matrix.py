"""The PerformanceAnalytics CoKurtosisMatrix function."""
import numpy as np
import pandas as pd
from rpy2 import robjects as ro
from rpy2.robjects import numpy2ri

from .rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from .xts import xts_from_df


def CoKurtosisMatrix(R: pd.DataFrame) -> np.ndarray:
    """Calculate CoKurtosisMatrix."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        with (ro.default_converter + numpy2ri.converter).context():
            return np.array(
                ro.r("CoKurtosisMatrix").rcall(  # type: ignore
                    (("R", xts_from_df(R)),),
                    lc,
                )
            )
