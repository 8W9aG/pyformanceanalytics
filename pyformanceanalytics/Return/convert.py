"""The PerformanceAnalytics Return.convert function."""
from __future__ import annotations

import pandas as pd

from ..backend.backend import Backend
from ..backend.R.Return.convert import convert as Rconvert
from .convert_destination_type import ConvertDestinationType


def convert(
    R: pd.DataFrame,
    destination_type: (str | ConvertDestinationType | None) = None,
    seed_value: (float | None) = None,
    initial: bool = True,
    backend: Backend = Backend.R,
) -> pd.DataFrame | float:
    """Calculate Return.convert."""
    if destination_type is None:
        destination_type = ConvertDestinationType.DISCRETE
    if backend == Backend.R:
        if isinstance(destination_type, ConvertDestinationType):
            destination_type = destination_type.value
        return Rconvert(
            R, destination_type=destination_type, seed_value=seed_value, initial=initial
        )
    raise NotImplementedError(
        f"Backend {backend.value} not implemented for Return.convert"
    )
