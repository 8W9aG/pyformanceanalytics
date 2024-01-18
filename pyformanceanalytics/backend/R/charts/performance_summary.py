"""The function for handling performance summaries charts."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image
from rpy2 import robjects as ro

from ..ggplot_img import ggplot_to_image
from ..rimports import (GGPLOT2_PACKAGE, GRIDEXTRA_PACKAGE,
                        PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present)
from ..xts import xts_from_df


def PerformanceSummary(
    R: pd.DataFrame,
    plot_width: int,
    plot_height: int,
    Rf: (pd.DataFrame | float),
    main: (str | None) = None,
    geometric: bool = True,
    methods: (str | None) = None,
    width: int = 0,
    event_labels: (bool | None) = None,
    ylog: bool = False,
    wealth_index: bool = False,
    gap: int = 12,
    begin: (list[str] | None) = None,
    legend_loc: (str | None) = None,
    p: float = 0.95,
) -> Image.Image:
    """Calculate charts.PerformanceSummary."""
    ensure_packages_present(
        [GGPLOT2_PACKAGE, GRIDEXTRA_PACKAGE, PERFORMANCE_ANALYTICS_PACKAGE]
    )
    if methods is None:
        methods = "none"
    if begin is None:
        begin = ["first", "axis"]
    if legend_loc is None:
        legend_loc = "topleft"
    with ro.local_context() as lc:
        return ggplot_to_image(
            ro.r("charts.PerformanceSummary").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("Rf", xts_from_df(Rf) if isinstance(Rf, pd.DataFrame) else Rf),
                    ("main", main),
                    ("geometric", geometric),
                    ("methods", methods),
                    ("width", width),
                    ("event.labels", event_labels),
                    ("ylog", ylog),
                    ("wealth.index", wealth_index),
                    ("gap", gap),
                    ("begin", ro.vectors.StrVector(begin)),
                    ("legend.loc", legend_loc),
                    ("p", p),
                    ("plot.engine", "ggplot2"),
                ),
                lc,
            ),
            plot_width,
            plot_height,
        )
