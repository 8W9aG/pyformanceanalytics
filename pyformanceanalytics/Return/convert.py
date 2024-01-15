"""The PerformanceAnalytics Return.convert function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects
from rpy2.robjects import pandas2ri

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df


def convert(R: pd.DataFrame, destination_type: Optional[str] = None, seed_value: Optional[float] = None, initial: bool = True) -> pd.DataFrame:
    """Calculate Return.convert."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if destination_type is None:
        destination_type = "discrete"
    with robjects.local_context() as lc:
        with (robjects.default_converter + pandas2ri.converter).context():
            return robjects.conversion.get_conversion().rpy2py(robjects.r("as.data.frame").rcall(
                (
                    ("x", robjects.r("Return.convert").rcall(
                        (
                            ("R", xts_from_df(R)),
                            ("destinationType", destination_type),
                            ("seedValue", seed_value),
                            ("initial", initial),
                        ),
                        lc,
                    )),
                ),
                lc,
            ))
