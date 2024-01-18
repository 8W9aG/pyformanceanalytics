"""Tests for the Frequency function."""
import pandas as pd
from pyformanceanalytics import Frequency


def test_frequency():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    R = df[["HAM1"]]
    assert Frequency(R) == 12.0
