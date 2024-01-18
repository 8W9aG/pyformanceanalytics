"""Tests for the CoKurtosis function."""
import pandas as pd
from pyformanceanalytics import CoKurtosis


def test_co_kurtosis():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    Ra = df[["HAM2"]]
    Rb = df[["SP500 TR"]]
    assert CoKurtosis(Ra, Rb) == 2.5790664604415916e-06
