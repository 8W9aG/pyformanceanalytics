"""Tests for the bull function."""
import pandas as pd
from pyformanceanalytics.CAPM.beta import bull


def test_bull():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert bull(Ra, Rb) == 0.30102037522580305
