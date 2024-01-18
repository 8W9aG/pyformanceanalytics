"""Tests for the centeredmoment function."""
import pandas as pd
from pyformanceanalytics import centeredmoment


def test_centeredmoment():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "c(HAM1 = 0.000651859786501377)": [0.0006518597865013774],
    }, index=["HAM1"])
    R = df[["HAM1"]]
    assert centeredmoment(R).equals(expected_df)
