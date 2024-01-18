"""The Performance Analytics chart.Correlation function."""
from __future__ import annotations

import pandas as pd
from PIL import Image
from rpy2 import robjects as ro

from ..plot_img import plot_to_image
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def Correlation(
    R: pd.DataFrame,
    method: str,
    plot_width: int,
    plot_height: int,
    histogram: bool = True,
) -> Image.Image:
    """Calculate chart.Correlation."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return plot_to_image(
            lambda: ro.r("chart.Correlation").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("histogram", histogram),
                    ("method", method),
                ),
                lc,
            ),
            plot_width,
            plot_height,
        )
