"""Tests for the HurstIndex function."""
import pandas as pd
from pyformanceanalytics import HurstIndex


def test_hurst_index():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.37964009397771764],
    }, index=["Hurst Index"])
    R = df[["HAM1"]]
    assert HurstIndex(R).equals(expected_df)
