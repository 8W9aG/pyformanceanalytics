"""Tests for the CalmarRatio function."""
import pandas as pd
from pyformanceanalytics import CalmarRatio


def test_calmar_ratio():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.9061697171079516],
    }, index=["Calmar Ratio"])
    R = df[["HAM1"]]
    assert CalmarRatio(R).equals(expected_df)
