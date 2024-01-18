"""Tests for the SemiSD function."""
import pandas as pd
from pyformanceanalytics import SemiSD


def test_semi_SD():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.019079503717896126],
    }, index=["Semi-Deviation"])
    R = df[["HAM1"]]
    assert SemiSD(R).equals(expected_df)
