"""Tests for the TimingRatio function."""
import pandas as pd
from pyformanceanalytics import TimingRatio


def test_timing_ratio():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    Ra = df[["HAM2"]]
    Rb = df[["SP500 TR"]]
    Rf = df[["US 3m TR"]]
    assert TimingRatio(Ra, Rb, Rf=Rf) == 7.4852242602397725
