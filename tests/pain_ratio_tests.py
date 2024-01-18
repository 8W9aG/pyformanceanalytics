"""Tests for the PainRatio function."""
import pandas as pd
from pyformanceanalytics import PainRatio


def test_pain_ratio():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [8.778852003691398],
    }, index=["Pain Index"])
    R = df[["HAM1"]]
    assert PainRatio(R).equals(expected_df)
