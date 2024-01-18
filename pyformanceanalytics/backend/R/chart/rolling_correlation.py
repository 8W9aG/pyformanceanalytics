"""The Performance Analytics chart.RollingCorrelation function."""
from __future__ import annotations

import pandas as pd
from PIL import Image
from rpy2 import robjects as ro

from ..plot_img import plot_ro, plot_to_image
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def RollingCorrelation(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    plot_width: int,
    plot_height: int,
    width: int = 12,
    xaxis: bool = True,
    legend_loc: (str | None) = None,
    colorset: (list[int] | None) = None,
) -> Image.Image:
    """Calculate chart.RollingCorrelation."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if colorset is None:
        colorset = list(range(1, 12))
    with ro.local_context() as lc:
        return plot_to_image(
            lambda: plot_ro(
                ro.r("chart.RollingCorrelation").rcall(  # type: ignore
                    (
                        ("Ra", xts_from_df(Ra)),
                        ("Rb", xts_from_df(Rb)),
                        ("width", width),
                        ("xaxis", xaxis),
                        ("legend.loc", legend_loc),
                        ("colorset", ro.vectors.IntVector(colorset)),
                    ),
                    lc,
                ),
                lc,
            ),
            plot_width,
            plot_height,
        )
