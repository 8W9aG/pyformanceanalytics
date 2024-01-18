"""The Performance Analytics chart.BarVaR function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.bar_va_r import BarVaR as RBarVaR


def BarVaR(
    R: pd.DataFrame,
    width: int = 0,
    gap: int = 12,
    methods: (list[str] | None) = None,
    p: float = 0.95,
    clean: (list[str] | None) = None,
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
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.BarVaR."""
    if backend == Backend.R:
        return RBarVaR(
            R,
            width=width,
            gap=gap,
            methods=methods,
            p=p,
            clean=clean,
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
