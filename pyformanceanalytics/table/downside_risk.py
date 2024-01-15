"""The PerformanceAnalytics table.DownsideRisk function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df


def downside_risk(R: pd.DataFrame, ci: float = 0.95, Rf: Optional[pd.DataFrame] = None, MAR: float = 0.1 / 12.0, p: float = 0.95, digits: int = 4) -> pd.DataFrame:
    """Calculate table.DownsideRisk."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("table.DownsideRisk").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("ci", ci),
                            ("Rf", 0 if Rf is None else xts_from_df(Rf)),
                            ("MAR", MAR),
                            ("p", p),
                            ("digits", digits),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
