"""The Performance Analytics chart.SnailTrail function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.snail_trail import SnailTrail as RSnailTrail
from .snail_trail_add_names import SnailTrailAddNames


def SnailTrail(
    R: pd.DataFrame,
    Rf: (pd.DataFrame | float) = 0.0,
    main: (str | None) = None,
    add_names: (str | SnailTrailAddNames | None) = None,
    xlab: (str | None) = None,
    ylab: (str | None) = None,
    add_sharpe: (list[int] | None) = None,
    colorset: (list[int] | None) = None,
    symbolset: int = 16,
    legend_loc: (str | None) = None,
    xlim: (float | None) = None,
    ylim: (float | None) = None,
    width: int = 12,
    stepsize: int = 12,
    lty: int = 1,
    lwd: int = 2,
    cex_axis: float = 0.8,
    cex_main: int = 1,
    cex_lab: int = 1,
    cex_text: float = 0.8,
    cex_legend: float = 0.8,
    element_color: (str | None) = None,
    plot_width: int = 512,
    plot_height: int = 512,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.SnailTrail."""
    if add_names is None:
        add_names = SnailTrailAddNames.ALL
    if backend == Backend.R:
        if isinstance(add_names, SnailTrailAddNames):
            add_names = add_names.value
        return RSnailTrail(
            R,
            add_names,
            plot_width,
            plot_height,
            Rf,
            main=main,
            xlab=xlab,
            ylab=ylab,
            add_sharpe=add_sharpe,
            colorset=colorset,
            symbolset=symbolset,
            legend_loc=legend_loc,
            xlim=xlim,
            ylim=ylim,
            width=width,
            stepsize=stepsize,
            lty=lty,
            lwd=lwd,
            cex_axis=cex_axis,
            cex_main=cex_main,
            cex_lab=cex_lab,
            cex_text=cex_text,
            cex_legend=cex_legend,
            element_color=element_color,
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for chart.SnailTrail"
    )
