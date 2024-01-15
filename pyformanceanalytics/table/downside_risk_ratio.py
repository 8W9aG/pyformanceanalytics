"""The PerformanceAnalytics table.DownsideRiskRatio function."""
import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df


def downside_risk_ratio(R: pd.DataFrame, MAR: float = 0.1 / 12.0, digits: int = 4) -> pd.DataFrame:
    """Calculate table.DownsideRiskRatio."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("table.DownsideRiskRatio").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("MAR", MAR),
                            ("digits", digits),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
