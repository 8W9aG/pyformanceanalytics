"""The Performance Analytics chart.RollingPerformance function."""
from __future__ import annotations

import pandas as pd
from PIL import Image
from rpy2 import robjects as ro

from ..plot_img import plot_ro, plot_to_image
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def RollingPerformance(
    R: pd.DataFrame,
    plot_width: int,
    plot_height: int,
    width: int = 12,
    fun: (str | None) = None,
    ylim: (float | None) = None,
    main: (str | None) = None,
) -> Image.Image:
    """Calculate chart.RollingPerformance."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if fun is None:
        fun = "Return.annualized"
    with ro.local_context() as lc:
        return plot_to_image(
            lambda: plot_ro(
                ro.r("chart.RollingPerformance").rcall(  # type: ignore
                    (
                        ("R", xts_from_df(R)),
                        ("width", width),
                        ("FUN", fun),
                        ("ylim", ylim),
                        ("main", main),
                    ),
                    lc,
                ),
                lc,
            ),
            plot_width,
            plot_height,
        )
