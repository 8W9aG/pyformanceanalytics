"""The Performance Analytics chart.ACF function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df
from ..plot_img import plot_to_image


def ACF(R: pd.DataFrame, maxlag: Optional[int] = None, elementcolor: Optional[str] = None, main: Optional[str] = None):
    """Calculate chart.ACF."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if elementcolor is None:
        elementcolor = "gray"
    with robjects.local_context() as lc:
        return plot_to_image(lambda: robjects.r("chart.ACF").rcall(
            (
                ("R", xts_from_df(R)),
                ("maxlag", maxlag),
                ("elementcolor", elementcolor),
                ("main", main),
            ),
            lc,
        ))