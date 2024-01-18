"""The Performance Analytics chart.Histogram function."""
# pylint: disable=too-many-locals
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image
from rpy2 import robjects as ro

from ..plot_img import plot_to_image
from ..rimports import PERFORMANCE_ANALYTICS_PACKAGE, ensure_packages_present
from ..xts import xts_from_df


def Histogram(
    R: pd.DataFrame,
    methods: list[str],
    plot_width: int,
    plot_height: int,
    breaks: (str | None) = None,
    main: (str | None) = None,
    xlab: (str | None) = None,
    ylab: (str | None) = None,
    show_outliers: bool = True,
    colorset: (list[str] | None) = None,
    border_col: (str | None) = None,
    lwd: int = 2,
    xlim: (float | None) = None,
    ylim: (float | None) = None,
    element_color: (str | None) = None,
    note_lines: (list[float] | None) = None,
    note_labels: (list[str] | None) = None,
    note_cex: float = 0.7,
    note_color: (str | None) = None,
    probability: bool = False,
    p: float = 0.95,
    cex_axis: float = 0.8,
    cex_legend: float = 0.8,
    cex_lab: int = 1,
    cex_main: int = 1,
    xaxis: bool = True,
    yaxis: bool = True,
) -> Image.Image:
    """Calculate chart.Histogram."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if breaks is None:
        breaks = "FD"
    if xlab is None:
        xlab = "Returns"
    if ylab is None:
        ylab = "Frequency"
    if colorset is None:
        colorset = [
            "lightgray",
            "#00008F",
            "#005AFF",
            "#23FFDC",
            "#ECFF13",
            "#FF4A00",
            "#800000",
        ]
    if border_col is None:
        border_col = "white"
    if note_color is None:
        note_color = "darkgrey"
    with ro.local_context() as lc:
        return plot_to_image(
            lambda: ro.r("chart.Histogram").rcall(  # type: ignore
                (
                    ("R", xts_from_df(R)),
                    ("main", main),
                    ("xlab", xlab),
                    ("ylab", ylab),
                    ("methods", ro.vectors.StrVector(methods)),
                    ("show.outliers", show_outliers),
                    ("colorset", ro.vectors.StrVector(colorset)),
                    ("border.col", border_col),
                    ("lwd", lwd),
                    ("xlim", xlim),
                    ("ylim", ylim),
                    ("element.color", element_color),
                    (
                        "note.lines",
                        None
                        if note_lines is None
                        else ro.vectors.FloatVector(note_lines),
                    ),
                    (
                        "note.labels",
                        None
                        if note_labels is None
                        else ro.vectors.StrVector(note_labels),
                    ),
                    ("note.cex", note_cex),
                    ("note.color", note_color),
                    ("probability", probability),
                    ("p", p),
                    ("cex.axis", cex_axis),
                    ("cex.legend", cex_legend),
                    ("cex.lab", cex_lab),
                    ("cex.main", cex_main),
                    ("xaxis", xaxis),
                    ("yaxis", yaxis),
                ),
                lc,
            ),
            plot_width,
            plot_height,
        )
