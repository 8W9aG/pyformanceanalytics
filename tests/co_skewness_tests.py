"""Tests for the CoSkewness function."""
import pandas as pd
from pyformanceanalytics import CoSkewness


def test_co_skewness():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    Ra = df[["HAM2"]]
    Rb = df[["SP500 TR"]]
    assert CoSkewness(Ra, Rb) == -2.1012892273018564e-06
