"""The Performance Analytics charts.RollingPerformance function."""
from __future__ import annotations

import pandas as pd
from PIL import Image
from rpy2 import robjects as ro

from ..plot_img import plot_to_image
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def RollingPerformance(
    R: pd.DataFrame,
    width: int = 12,
    Rf: (pd.DataFrame | None) = None,
    main: (str | None) = None,
    event_labels: (bool | None) = None,
    legend_loc: (str | None) = None,
) -> Image.Image:
    """Calculate charts.RollingPerformance."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return plot_to_image(
            lambda: ro.r("charts.RollingPerformance").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("width", width),
                    ("Rf", 0 if Rf is None else xts_from_df(Rf)),
                    ("main", main),
                    ("event.labels", event_labels),
                    ("legend.loc", legend_loc),
                ),
                lc,
            )
        )