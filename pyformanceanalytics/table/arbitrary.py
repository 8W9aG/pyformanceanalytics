"""The PerformanceAnalytics table.Arbitrary function."""
from typing import Optional, List

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri
from rpy2.robjects.vectors import StrVector

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df


def arbitrary(R: pd.DataFrame, metrics: Optional[List[str]] = None, metrics_names: Optional[List[str]] = None) -> pd.DataFrame:
    """Calculate table.Arbitrary."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if metrics is None:
        metrics = ["mean", "sd"]
    if metrics_names is None:
        metrics_names = ["Average Return", "Standard Deviation"]
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("table.Arbitrary").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("metrics", StrVector(metrics)),
                            ("metricsNames", StrVector(metrics_names)),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
