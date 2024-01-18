"""Tests for the AverageRecovery function."""
import pandas as pd
from pyformanceanalytics import AverageRecovery


def test_average_recovery():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1": [2.466666666666667],
        "HAM2": [3.384615384615385],
        "HAM3": [3.7142857142857144],
        "HAM4": [4.53846153846154],
        "HAM5": [23.5],
        "HAM6": [3.8571428571428568],
        "EDHEC.LS.EQ": [2.5384615384615383],
        "SP500.TR": [5.666666666666666],
        "US.10Y.TR": [3.866666666666667],
        "US.3m.TR": [0.0],
    }, index=["Average Recovery"])
    assert AverageRecovery(df).equals(expected_df)
