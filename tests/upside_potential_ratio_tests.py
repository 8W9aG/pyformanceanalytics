"""Tests for the UpsidePotentialRatio function."""
import pandas as pd
from pyformanceanalytics import UpsidePotentialRatio


def test_ulcer_index():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.7503177359620867],
    }, index=["Upside Potential (MAR = 0%)"])
    R = df[["HAM1"]]
    assert UpsidePotentialRatio(R).equals(expected_df)
