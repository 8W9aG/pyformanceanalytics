"""Tests for the UpsideFrequency function."""
import pandas as pd
from pyformanceanalytics import UpsideFrequency


def test_upside_frequency():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    R = df[["HAM1"]]
    assert UpsideFrequency(R) == 0.7424242424242424
