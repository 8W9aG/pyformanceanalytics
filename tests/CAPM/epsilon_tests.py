"""Tests for the epsilon function."""
import pandas as pd
from pyformanceanalytics.CAPM import epsilon


def test_epsilon():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df[df.index.year == 1996]
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert epsilon(Ra, Rb) == 0.07425365847503913
