"""The Performance Analytics chart.ACFplus function."""
from __future__ import annotations

import pandas as pd
from PIL import Image
from rpy2 import robjects as ro

from ..plot_img import plot_to_image
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def ACFplus(
    R: pd.DataFrame,
    maxlag: (int | None) = None,
    elementcolor: (str | None) = None,
    main: (str | None) = None,
) -> Image.Image:
    """Calculate chart.ACFplus."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if elementcolor is None:
        elementcolor = "gray"
    with ro.local_context() as lc:
        return plot_to_image(
            lambda: ro.r("chart.ACFplus").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("maxlag", maxlag),
                    ("elementcolor", elementcolor),
                    ("main", main),
                ),
                lc,
            )
        )
