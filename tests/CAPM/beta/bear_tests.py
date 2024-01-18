"""Tests for the bear function."""
import pandas as pd
from pyformanceanalytics.CAPM.beta import bear


def test_bear():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert bear(Ra, Rb) == 0.42573339132031507
