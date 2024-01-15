"""The PerformanceAnalytics M2Sortino function."""
import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def M2_sortino(Ra: pd.DataFrame, Rb: pd.DataFrame, MAR: float) -> pd.DataFrame:
    """Calculate M2Sortino."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("M2Sortino").rcall(
                        (
                            ("Ra", xts_from_df(Ra)),
                            ("Rb", xts_from_df(Rb)),
                            ("MAR", MAR),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
