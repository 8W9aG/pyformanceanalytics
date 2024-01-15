"""The PerformanceAnalytics M2.shrink function."""
from typing import Optional

import numpy as np
import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri, numpy2ri

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df


def shrink(R: pd.DataFrame, targets: int = 1, f: Optional[pd.DataFrame] = None) -> pd.DataFrame:
    """Calculate M2.shrink."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + numpy2ri.converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("M2.shrink").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("targets", targets),
                            ("f", f),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))