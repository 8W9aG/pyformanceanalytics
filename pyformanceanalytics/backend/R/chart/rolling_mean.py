"""The Performance Analytics chart.RollingMean function."""
from __future__ import annotations

import pandas as pd
from PIL import Image
from rpy2 import robjects as ro

from ..plot_img import plot_ro, plot_to_image
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def RollingMean(
    R: pd.DataFrame,
    plot_width: int,
    plot_height: int,
    width: int = 12,
    xaxis: bool = True,
    ylim: (float | None) = None,
    lwd: (list[int] | None) = None,
) -> Image.Image:
    """Calculate chart.RollingMean."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if lwd is None:
        lwd = [2, 1, 1]
    with ro.local_context() as lc:
        return plot_to_image(
            lambda: plot_ro(
                ro.r("chart.RollingMean").rcall(  # type: ignore
                    (
                        ("R", xts_from_df(R)),
                        ("width", width),
                        ("xaxis", xaxis),
                        ("ylim", ylim),
                        ("lwd", ro.vectors.IntVector(lwd)),
                    ),
                    lc,
                ),
                lc,
            ),
            plot_width,
            plot_height,
        )
