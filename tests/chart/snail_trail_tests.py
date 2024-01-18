"""Tests for the SnailTrail function."""
import pandas as pd
from pyformanceanalytics.chart import SnailTrail


def test_snail_trail():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    assert SnailTrail(df) is not None
