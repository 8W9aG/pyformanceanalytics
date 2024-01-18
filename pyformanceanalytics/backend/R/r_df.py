"""A function for converting an r object to a dataframe."""
from __future__ import annotations

import pandas as pd
from rpy2 import robjects as ro
from rpy2.robjects import pandas2ri


def as_data_frame(x: ro.RObject, env: ro.Environment) -> pd.DataFrame:
    """Convert an r object to a dataframe."""
    with (ro.default_converter + pandas2ri.converter).context():  # type: ignore
        return ro.conversion.get_conversion().rpy2py(
            ro.r("as.data.frame").rcall(  # type: ignore
                (
                    (
                        "x",
                        x,
                    ),
                ),
                env,
            )
        )


def as_data_frame_or_float(x: ro.RObject, env: ro.Environment) -> pd.DataFrame | float:
    """Convert an r object to a dataframe."""
    df = as_data_frame(x, env)
    if df.shape[0] == 1 and df.shape[1] == 1:
        return df.iat[0, 0]
    return df
