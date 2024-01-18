"""Tests for the kurtosis function."""
import pandas as pd
from pyformanceanalytics import kurtosis


def test_kurtosis():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    R = df[["HAM1"]]
    assert kurtosis(R) == 5.361588759837649
