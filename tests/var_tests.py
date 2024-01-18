"""Tests for the VaR function."""
import pandas as pd
from pyformanceanalytics import VaR


def test_var():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [0.034229548148495506],
    }, index=["VaR"])
    R = df[["HAM1"]]
    assert VaR(R).equals(expected_df)
