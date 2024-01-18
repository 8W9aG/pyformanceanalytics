"""Tests for the BernardoLedoitRatio function."""
import pandas as pd
from pyformanceanalytics import BernardoLedoitRatio


def test_bernardo_ledoit_ratio():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    R = df[df.index.year == 1996][["HAM1"]]
    assert BernardoLedoitRatio(R) == 4.598337950138505
