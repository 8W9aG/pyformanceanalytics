"""Tests for the UlcerIndex function."""
import pandas as pd
from pyformanceanalytics import UlcerIndex


def test_ulcer_index():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.03620029685418974],
    }, index=["Ulcer Index"])
    R = df[["HAM1"]]
    assert UlcerIndex(R).equals(expected_df)
