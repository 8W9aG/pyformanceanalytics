"""Tests for the Omega function."""
import pandas as pd
from pyformanceanalytics import Omega


def test_omega():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [3.1906893464637416],
    }, index=["Omega (L = 0%)"])
    R = df[["HAM1"]]
    assert Omega(R).equals(expected_df)
