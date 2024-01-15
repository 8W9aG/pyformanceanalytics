"""The PerformanceAnalytics M4.shrink function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri, numpy2ri

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df


def shrink(R: pd.DataFrame, targets: int = 1, f: Optional[pd.DataFrame] = None, as_mat: bool = True) -> pd.DataFrame:
    """Calculate M4.shrink."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + numpy2ri.converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("M4.shrink").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("targets", targets),
                            ("f", f),
                            ("as.mat", as_mat),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
