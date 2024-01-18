"""Tests for the lpm function."""
import pandas as pd
from pyformanceanalytics import lpm


def test_lpm():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.0008457369696969698],
    }, index=["LPM"])
    R = df[["HAM1"]]
    assert lpm(R).equals(expected_df)
