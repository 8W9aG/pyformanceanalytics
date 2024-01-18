"""Tests for the TreynorRatio function."""
import pandas as pd
from pyformanceanalytics import TreynorRatio


def test_treynor_ratio():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert TreynorRatio(Ra, Rb) == 0.35210148457034324
