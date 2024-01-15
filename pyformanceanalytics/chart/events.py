"""The Performance Analytics chart.Events function."""
import datetime
from typing import Optional, List

import pandas as pd
from rpy2 import robjects
from rpy2.robjects.vectors import StrVector

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df
from ..plot_img import plot_to_image


def events(R: pd.DataFrame, dates: List[datetime.date], prior: int = 12, post: int = 12, main: Optional[str] = None, xlab: Optional[str] = None):
    """Calculate chart.Events."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with robjects.local_context() as lc:
        return plot_to_image(lambda: robjects.r("plot").rcall(
            (
                ("x", robjects.r("chart.Events").rcall(
                    (
                        ("R", xts_from_df(R)),
                        ("dates", StrVector([x.strftime("%Y-%m-%d") for x in dates])),
                        ("prior", prior),
                        ("post", post),
                        ("main", main),
                        ("xlab", xlab),
                    ),
                    lc,
                )),
            ),
            lc,
        ))
