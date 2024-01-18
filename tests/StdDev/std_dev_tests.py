"""Tests for the StdDev function."""
import pandas as pd
from pyformanceanalytics.StdDev import StdDev


def test_std_dev():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "V1": [0.025628808310297378],
    }, index=["StdDev"])
    R = df[["HAM1"]]
    assert StdDev(R).equals(expected_df)
