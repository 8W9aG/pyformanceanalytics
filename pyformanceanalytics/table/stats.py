"""The PerformanceAnalytics table.Stats function."""
import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df


def stats(R: pd.DataFrame, ci: float = 0.95, digits: int = 4) -> pd.DataFrame:
    """Calculate table.Stats."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("table.Stats").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("ci", ci),
                            ("digits", digits),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
