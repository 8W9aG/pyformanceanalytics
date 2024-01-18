"""Tests for the DownsideDeviation function."""
import pandas as pd
from pyformanceanalytics import DownsideDeviation


def test_downside_deviation():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    R = df[["HAM1"]]
    assert DownsideDeviation(R) == 0.014540778604471028
