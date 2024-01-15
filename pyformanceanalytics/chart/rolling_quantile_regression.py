"""The Performance Analytics chart.RollingQuantileRegression function."""
from typing import Optional, List

import pandas as pd
from rpy2 import robjects
from rpy2.robjects.vectors import StrVector

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE, QUANTREG_PACKAGE
from ..xts import xts_from_df
from ..plot_img import plot_to_image


def rolling_quantile_regression(Ra: pd.DataFrame, Rb: pd.DataFrame, width: int = 12, Rf: Optional[pd.DataFrame] = None, attribute: Optional[List[str]] = None, main: Optional[str] = None, na_pad: bool = True):
    """Calculate chart.RollingQuantileRegression."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE, QUANTREG_PACKAGE])
    if attribute is None:
        attribute = ["Beta", "Alpha", "R-Squared"]
    with robjects.local_context() as lc:
        return plot_to_image(lambda: robjects.r("plot").rcall(
            (
                ("x", robjects.r("chart.RollingQuantileRegression").rcall(
                    (
                        ("Ra", xts_from_df(Ra)),
                        ("Rb", xts_from_df(Rb)),
                        ("width", width),
                        ("Rf", 0 if Rf is None else xts_from_df(Rf)),
                        ("attribute", StrVector(attribute)),
                        ("main", main),
                        ("na.pad", na_pad),
                    ),
                    lc,
                )),
            ),
            lc,
        ))
