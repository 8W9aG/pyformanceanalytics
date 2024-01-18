"""Tests for the DownsideFrequency function."""
import pandas as pd
from pyformanceanalytics import DownsideFrequency


def test_downside_frequency():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df[df.index.year == 1996]
    R = df[["HAM1"]]
    assert DownsideFrequency(R) == 0.25
