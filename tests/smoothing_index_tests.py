"""Tests for the SmoothingIndex function."""
import pandas as pd
from pyformanceanalytics import SmoothingIndex


def test_smoothing_index():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "c(HAM1 = 0.62110696359369)": [0.6211069635936899],
    }, index=["HAM1"])
    R = df[["HAM1"]]
    assert SmoothingIndex(R).equals(expected_df)
