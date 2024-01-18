"""Tests for the BurkeRatio function."""
import pandas as pd
from pyformanceanalytics import BurkeRatio


def test_burke_ratio():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    R = df[df.index.year == 1996][["HAM1"]]
    assert BurkeRatio(R) == 4.779747402698481
