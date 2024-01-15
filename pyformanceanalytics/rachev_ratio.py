"""The PerformanceAnalytics RachevRatio function."""
import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def rachev_ratio(R: pd.DataFrame, alpha: float = 0.1, beta: float = 0.1, rf: float = 0.0, SE: bool = False) -> pd.DataFrame:
    """Calculate RachevRatio."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("RachevRatio").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("alpha", alpha),
                            ("beta", beta),
                            ("rf", rf),
                            ("SE", SE),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
