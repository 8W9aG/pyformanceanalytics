"""The Performance Analytics chart.Histogram function."""
from typing import Optional, List

import pandas as pd
from rpy2 import robjects
from rpy2.robjects.vectors import StrVector, FloatVector

from ..rimports import ensure_packages_present, PERFORMANCE_ANALYTICS_PACKAGE
from ..xts import xts_from_df
from ..plot_img import plot_to_image


def histogram(
        R: pd.DataFrame,
        breaks: Optional[str] = None,
        main: Optional[str] = None,
        xlab: Optional[str] = None,
        ylab: Optional[str] = None,
        methods: Optional[List[str]] = None,
        show_outliers: bool = True,
        colorset: Optional[List[str]] = None,
        border_col: Optional[str] = None,
        lwd: int = 2,
        xlim: Optional[float] = None,
        ylim: Optional[float] = None,
        element_color: Optional[str] = None,
        note_lines: Optional[List[float]] = None,
        note_labels: Optional[List[str]] = None,
        note_cex: float = 0.7,
        note_color: Optional[str] = None,
        probability: bool = False,
        p: float = 0.95,
        cex_axis: float = 0.8,
        cex_legend: float = 0.8,
        cex_lab: int = 1,
        cex_main: int = 1,
        xaxis: bool = True,
        yaxis: bool = True):
    """Calculate chart.Histogram."""
    ensure_packages_present([PERFORMANCE_ANALYTICS_PACKAGE])
    if breaks is None:
        breaks = "FD"
    if xlab is None:
        xlab = "Returns"
    if ylab is None:
        ylab = "Frequency"
    if methods is None:
        methods = ["none", "add.density", "add.normal", "add.centered", "add.cauchy", "add.sst", "add.rug", "add.risk", "add.qqplot"]
    if colorset is None:
        colorset = ["lightgray", "#00008F", "#005AFF", "#23FFDC", "#ECFF13", "#FF4A00", "#800000"]
    if border_col is None:
        border_col = "white"
    if note_color is None:
        note_color = "darkgrey"
    with robjects.local_context() as lc:
        return plot_to_image(lambda: robjects.r("chart.Histogram").rcall(
            (
                ("R", xts_from_df(R)),
                ("main", main),
                ("xlab", xlab),
                ("ylab", ylab),
                ("methods", StrVector(methods)),
                ("show.outliers", show_outliers),
                ("colorset", StrVector(colorset)),
                ("border.col", border_col),
                ("lwd", lwd),
                ("xlim", xlim),
                ("ylim", ylim),
                ("element.color", element_color),
                ("note.lines", None if note_lines is None else FloatVector(note_lines)),
                ("note.labels", None if note_labels is None else StrVector(note_labels)),
                ("note.cex", note_cex),
                ("note.color", note_color),
                ("probability", probability),
                ("p", p),
                ("cex.axis", cex_axis),
                ("cex.lab", cex_lab),
                ("cex.main", cex_main),
                ("xaxis", xaxis),
                ("yaxis", yaxis),
            ),
            lc,
        ))
