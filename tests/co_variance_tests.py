"""Tests for the CoVariance function."""
import pandas as pd
from pyformanceanalytics import CoVariance


def test_co_variance():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert CoVariance(Ra, Rb) == 0.0007271005225550965
