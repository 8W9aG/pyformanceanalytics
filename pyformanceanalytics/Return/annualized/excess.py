"""The PerformanceAnalytics Return.annualized.excess function."""
import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from ...rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ...xts import xts_from_df


def excess(Rp: pd.DataFrame, Rb: pd.DataFrame, geometric: bool = True) -> pd.DataFrame:
    """Calculate Return.annualized.excess."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("Return.annualized.excess").rcall(
                        (
                            ("Rp", xts_from_df(Rp)),
                            ("Rb", xts_from_df(Rb)),
                            ("geometric", geometric),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
