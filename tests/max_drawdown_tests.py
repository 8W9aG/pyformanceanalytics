"""Tests for the maxDrawdown function."""
import pandas as pd
from pyformanceanalytics import maxDrawdown


def test_max_drawdown():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    R = df[["HAM1"]]
    assert maxDrawdown(R) == 0.1517729054802286
