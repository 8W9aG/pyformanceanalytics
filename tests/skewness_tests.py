"""Tests for the skewness function."""
import pandas as pd
from pyformanceanalytics import skewness


def test_skewness():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    R = df[["HAM1"]]
    assert skewness(R) == -0.6588444914834326
