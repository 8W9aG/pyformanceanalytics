"""The Performance Analytics chart.Bar function."""
from __future__ import annotations

import pandas as pd
from PIL import Image
from rpy2 import robjects as ro

from ..ggplot_img import ggplot_to_image
from ..rimports import (GGPLOT2_PACKAGE, PERFORMANCE_ANALYTICS_PACKAGE,
                        ensure_packages_present)
from ..xts import xts_from_df


def Bar(
    R: pd.DataFrame, plot_width: int, plot_height: int, legend_loc: (str | None) = None
) -> Image.Image:
    """Calculate chart.Bar."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE, GGPLOT2_PACKAGE])
    with ro.local_context() as lc:
        return ggplot_to_image(
            ro.r("chart.Bar").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("legend.loc", legend_loc),
                    ("plot.engine", "ggplot2"),
                ),
                lc,
            ),
            plot_width,
            plot_height,
        )
