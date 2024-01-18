"""Tests for the SemiVariance function."""
import pandas as pd
from pyformanceanalytics import SemiVariance


def test_semi_variance():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.02698249292119659],
    }, index=["Semi-Variance"])
    R = df[["HAM1"]]
    assert SemiVariance(R).equals(expected_df)
