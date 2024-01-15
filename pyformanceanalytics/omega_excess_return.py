"""The PerformanceAnalytics OmegaExcessReturn function."""
import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from .rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from .xts import xts_from_df


def omega_excess_return(
        Ra: pd.DataFrame,
        Rb: pd.DataFrame,
        MAR: float = 0.0) -> pd.DataFrame:
    """Calculate OmegaExcessReturn."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("OmegaExcessReturn").rcall(
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
