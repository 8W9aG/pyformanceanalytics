"""The Performance Analytics chart.RollingQuantileRegression function."""
from __future__ import annotations

import pandas as pd
from PIL import Image
from rpy2 import robjects as ro

from ..plot_img import plot_ro, plot_to_image
from ..rimports import (PERFORMANCE_ANALYTICS_PACKAGE, QUANTREG_PACKAGE,
                        ensure_packages_present)
from ..xts import xts_from_df


def RollingQuantileRegression(
    Ra: pd.DataFrame,
    Rb: pd.DataFrame,
    attribute: str,
    plot_width: int,
    plot_height: int,
    Rf: (pd.DataFrame | float),
    width: int = 12,
    main: (str | None) = None,
    na_pad: bool = True,
) -> Image.Image:
    """Calculate chart.RollingQuantileRegression."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE, QUANTREG_PACKAGE])
    with ro.local_context() as lc:
        return plot_to_image(
            lambda: plot_ro(
                ro.r("chart.RollingQuantileRegression").rcall(  # type: ignore
                    (
                        ("Ra", xts_from_df(Ra)),
                        ("Rb", xts_from_df(Rb)),
                        ("width", width),
                        ("Rf", xts_from_df(Rf) if isinstance(Rf, pd.DataFrame) else Rf),
                        ("attribute", ro.vectors.StrVector([attribute])),
                        ("main", main),
                        ("na.pad", na_pad),
                    ),
                    lc,
                ),
                lc,
            ),
            plot_width,
            plot_height,
        )
