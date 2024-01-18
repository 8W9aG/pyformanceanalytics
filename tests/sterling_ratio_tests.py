"""Tests for the SterlingRatio function."""
import pandas as pd
from pyformanceanalytics import SterlingRatio


def test_sterling_ratio():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.5462542149296952],
    }, index=["Sterling Ratio (Excess = 10%)"])
    R = df[["HAM1"]]
    assert SterlingRatio(R).equals(expected_df)
