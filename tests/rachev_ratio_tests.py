"""Tests for the RachevRatio function."""
import pandas as pd
from pyformanceanalytics import RachevRatio


def test_rachev_ratio():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [1.4825278810408924],
    }, index=["RachevRatio"])
    R = df[["HAM1"]]
    assert RachevRatio(R).equals(expected_df)
