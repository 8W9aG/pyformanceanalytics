"""Tests for the SortinoRatio function."""
import pandas as pd
from pyformanceanalytics import SortinoRatio


def test_sortino_ratio():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.7649334038623787],
    }, index=["Sortino Ratio (MAR = 0%)"])
    R = df[["HAM1"]]
    assert SortinoRatio(R).equals(expected_df)
