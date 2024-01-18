"""The Performance Analytics chart.CumReturns function."""
from __future__ import annotations

import pandas as pd
from PIL import Image
from rpy2 import robjects as ro

from ..plot_img import plot_ro, plot_to_image
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def CumReturns(
    R: pd.DataFrame,
    begin: str,
    plot_width: int,
    plot_height: int,
    wealth_index: bool = False,
    geometric: bool = True,
    legend_loc: (str | None) = None,
) -> Image.Image:
    """Calculate chart.CumReturns."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return plot_to_image(
            lambda: plot_ro(
                ro.r("chart.CumReturns").rcall(  # type: ignore
                    (
                        ("R", xts_from_df(R)),
                        ("wealth.index", wealth_index),
                        ("geometric", geometric),
                        ("legend.loc", legend_loc),
                        ("begin", ro.vectors.StrVector([begin])),
                    ),
                    lc,
                ),
                lc,
            ),
            plot_width,
            plot_height,
        )
