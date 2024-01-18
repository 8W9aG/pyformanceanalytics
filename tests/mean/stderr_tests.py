"""Tests for the stderr function."""
import pandas as pd
from pyformanceanalytics.mean import stderr


def test_stderr():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.0022307014377972384],
    }, index=["Standard Error"])
    R = df[["HAM1"]]
    assert stderr(R).equals(expected_df)
