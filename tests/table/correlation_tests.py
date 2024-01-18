"""Tests for the Correlation function."""
import pandas as pd
from pyformanceanalytics.table import Correlation

def test_correlation():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "Correlation": [0.660067122891702],
        "p-value": [7.397842246414847e-18],
        "Lower CI": [0.5513837557398673],
        "Upper CI": [0.7467191428465585],
    }, index=["HAM1 to SP500.TR"])
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert Correlation(Ra, Rb).equals(expected_df)
