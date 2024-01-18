"""Tests for the Drawdown function."""
import pandas as pd
from pyformanceanalytics.chart import Drawdown


def test_drawdown():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    assert Drawdown(df) is not None
