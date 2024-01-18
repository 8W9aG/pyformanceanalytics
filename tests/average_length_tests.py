"""Tests for the AverageLength function."""
import pandas as pd
from pyformanceanalytics import AverageLength


def test_average_length():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [4.933333333333334],
        "HAM2": [8.076923076923077],
        "HAM3": [7.0],
        "HAM4": [7.846153846153848],
        "HAM5": [36.5],
        "HAM6": [5.857142857142858],
        "EDHEC.LS.EQ": [5.9230769230769225],
        "SP500.TR": [9.083333333333334],
        "US.10Y.TR": [7.533333333333334],
        "US.3m.TR": [0.0],
    }, index=["Average Length"])
    assert AverageLength(df).equals(expected_df)
