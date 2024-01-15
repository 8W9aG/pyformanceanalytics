"""The PerformanceAnalytics centeredcomoment function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def centeredcomoment(Ra: pd.DataFrame, Rb: pd.DataFrame, p1: float, p2: float, normalize: bool = False) -> pd.DataFrame:
    """Calculate centeredcomoment."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("centeredcomoment").rcall(
                        (
                            ("Ra", xts_from_df(Ra)),
                            ("Rb", xts_from_df(Rb)),
                            ("p1", p1),
                            ("p2", p2),
                            ("normalize", normalize),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
