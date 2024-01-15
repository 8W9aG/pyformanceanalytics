"""The Performance Analytics chart.Bar function."""
from typing import Optional

import pandas as pd
from rpy2 import robjects

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE, GGPLOT2_PACKAGE
from ..xts import xts_from_df
from ..ggplot_img import ggplot_to_image


def bar(R: pd.DataFrame, legend_loc: Optional[str] = None):
    """Calculate chart.Bar."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE, GGPLOT2_PACKAGE])
    with robjects.local_context() as lc:
        plt = robjects.r("chart.Bar").rcall(
            (
                ("R", xts_from_df(R)),
                ("legend.loc", legend_loc),
                ("plot.engine", "ggplot2"),
            ),
            lc,
        )
        return ggplot_to_image(plt)
