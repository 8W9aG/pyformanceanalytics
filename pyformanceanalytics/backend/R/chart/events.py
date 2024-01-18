"""The Performance Analytics chart.Events function."""
from __future__ import annotations

import datetime

import pandas as pd
from PIL import Image
from rpy2 import robjects as ro

from ..plot_img import plot_ro, plot_to_image
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def Events(
    R: pd.DataFrame,
    dates: list[datetime.date],
    plot_width: int,
    plot_height: int,
    prior: int = 12,
    post: int = 12,
    main: (str | None) = None,
    xlab: (str | None) = None,
) -> Image.Image:
    """Calculate chart.Events."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    with ro.local_context() as lc:
        return plot_to_image(
            lambda: plot_ro(
                ro.r("chart.Events").rcall(  # type: ignore
                    (
                        ("R", xts_from_df(R)),
                        (
                            "dates",
                            ro.vectors.StrVector(
                                [x.strftime("%Y-%m-%d") for x in dates]
                            ),
                        ),
                        ("prior", prior),
                        ("post", post),
                        ("main", main),
                        ("xlab", xlab),
                    ),
                    lc,
                ),
                lc,
            ),
            plot_width,
            plot_height,
        )
