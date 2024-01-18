"""Tests for the MeanAbsoluteDeviation function."""
import pandas as pd
from pyformanceanalytics import MeanAbsoluteDeviation


def test_mean_absolute_deviation():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    R = df[["HAM1"]]
    assert MeanAbsoluteDeviation(R) == 0.01818636363636364
