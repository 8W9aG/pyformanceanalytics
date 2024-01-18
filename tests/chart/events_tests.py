"""Tests for the Events function."""
import datetime

import pandas as pd
from pyformanceanalytics.chart import Events


def test_events():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    assert Events(df, [datetime.date(2006, 8, 31)]) is not None
