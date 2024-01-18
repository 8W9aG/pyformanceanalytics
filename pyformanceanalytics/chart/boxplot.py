"""The Performance Analytics chart.Boxplot function."""
# pylint: disable=too-many-arguments
from __future__ import annotations

import pandas as pd
from PIL import Image

from ..backend.backend import Backend
from ..backend.R.chart.boxplot import Boxplot as RBoxplot
from .boxplot_sort_by import BoxplotSortBy


def Boxplot(
    R: pd.DataFrame,
    names: bool = True,
    as_tufte: bool = True,
    sort_by: (str | BoxplotSortBy | None) = None,
    colorset: (str | None) = None,
    symbol_color: (str | None) = None,
    mean_symbol: int = 1,
    median_symbol: (str | None) = None,
    outlier_symbol: int = 1,
    show_data: (list[int] | None) = None,
    add_mean: bool = True,
    sort_ascending: bool = False,
    xlab: (str | None) = None,
    main: (str | None) = None,
    element_color: (str | None) = None,
    plot_width: int = 512,
    plot_height: int = 512,
    backend: Backend = Backend.R,
) -> Image.Image:
    """Calculate chart.Boxplot."""
    if backend == Backend.R:
        if isinstance(sort_by, BoxplotSortBy):
            sort_by = sort_by.value
        return RBoxplot(
            R,
            plot_width,
            plot_height,
            names=names,
            as_tufte=as_tufte,
            sort_by=sort_by,
            colorset=colorset,
            symbol_color=symbol_color,
            mean_symbol=mean_symbol,
            median_symbol=median_symbol,
            outlier_symbol=outlier_symbol,
            show_data=show_data,
            add_mean=add_mean,
            sort_ascending=sort_ascending,
            xlab=xlab,
            main=main,
            element_color=element_color,
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for chart.Boxplot"
    )
