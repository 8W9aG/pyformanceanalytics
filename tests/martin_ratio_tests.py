"""Tests for the MartinRatio function."""
import pandas as pd
from pyformanceanalytics import MartinRatio


def test_martin_ratio():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [3.7991956634397868],
    }, index=["Ulcer Index"])
    R = df[["HAM1"]]
    assert MartinRatio(R).equals(expected_df)
