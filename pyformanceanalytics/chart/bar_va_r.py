"""The Performance Analytics chart.BarVaR function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.bar_va_r import BarVaR as RBarVaR
from .bar_va_r_methods import BarVaRMethod
from .clean import Clean


def BarVaR(
    R: pd.DataFrame,
    width: int = 0,
    gap: int = 12,
    methods: (list[str | BarVaRMethod] | None) = None,
    p: float = 0.95,
    clean: (str | Clean | None) = None,
    all_: bool = False,
    show_clean: bool = False,
    show_horizontal: bool = False,
    show_symmetric: bool = False,
    show_endvalue: bool = False,
    show_greenredbars: bool = False,
    legend_loc: (str | None) = None,
    lwd: int = 2,
    lty: int = 1,
    ypad: int = 0,
    legend_cex: float = 0.8,
    plot_width: int = 512,
    plot_height: int = 512,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.BarVaR."""
    if methods is None:
        methods = [
            BarVaRMethod.NONE,
            BarVaRMethod.MODIFIEDVAR,
            BarVaRMethod.GAUSSIANVAR,
            BarVaRMethod.HISTORICALVAR,
            BarVaRMethod.STDDEV,
            BarVaRMethod.MODIFIEDES,
            BarVaRMethod.GAUSSIANES,
            BarVaRMethod.HISTORICALES,
        ]
    if clean is None:
        clean = Clean.NONE
    if backend == Backend.R:
        if isinstance(clean, Clean):
            clean = clean.value
        return RBarVaR(
            R,
            [x.value if isinstance(x, BarVaRMethod) else x for x in methods],
            clean,
            plot_width,
            plot_height,
            width=width,
            gap=gap,
            p=p,
            all_=all_,
            show_clean=show_clean,
            show_horizontal=show_horizontal,
            show_symmetric=show_symmetric,
            show_endvalue=show_endvalue,
            show_greenredbars=show_greenredbars,
            legend_loc=legend_loc,
            lwd=lwd,
            lty=lty,
            ypad=ypad,
            legend_cex=legend_cex,
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for chart.BarVaR"
    )
