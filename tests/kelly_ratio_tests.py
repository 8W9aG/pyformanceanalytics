"""Tests for the KellyRatio function."""
import pandas as pd
from pyformanceanalytics import KellyRatio


def test_kelly_ratio():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [8.466900716926263],
    }, index=["Kelly Ratio"])
    R = df[["HAM1"]]
    assert KellyRatio(R).equals(expected_df)
