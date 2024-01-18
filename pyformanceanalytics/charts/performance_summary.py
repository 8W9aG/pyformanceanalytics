"""The function for handling performance summaries charts."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.charts.performance_summary import \
    PerformanceSummary as RPerformanceSummary


def PerformanceSummary(
    R: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
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
    plot_width: int = 512,
    plot_height: int = 512,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate charts.PerformanceSummary."""
    if backend == Backend.R:
        return RPerformanceSummary(
            R,
            plot_width,
            plot_height,
            Rf,
            main=main,
            geometric=geometric,
            methods=methods,
            width=width,
            event_labels=event_labels,
            ylog=ylog,
            wealth_index=wealth_index,
            gap=gap,
            begin=begin,
            legend_loc=legend_loc,
            p=p,
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for charts.PerformanceSummary"
    )
