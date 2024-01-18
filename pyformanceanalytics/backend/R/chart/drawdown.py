"""The Performance Analytics chart.Drawdown function."""
from __future__ import annotations

import pandas as pd
from PIL import Image
from rpy2 import robjects as ro

from ..plot_img import plot_ro, plot_to_image
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def Drawdown(
    R: pd.DataFrame,
    plot_width: int,
    plot_height: int,
    geometric: bool = True,
    legend_loc: (str | None) = None,
) -> Image.Image:
    """Calculate chart.Drawdown."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return plot_to_image(
            lambda: plot_ro(
                ro.r("chart.Drawdown").rcall(  # type: ignore
                    (
                        ("R", xts_from_df(R)),
                        ("geometric", geometric),
                        ("legend.loc", legend_loc),
                    ),
                    lc,
                ),
                lc,
            ),
            plot_width,
            plot_height,
        )
