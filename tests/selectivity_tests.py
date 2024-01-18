"""Tests for the Selectivity function."""
import pandas as pd
from pyformanceanalytics import Selectivity


def test_selectivity():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert Selectivity(Ra, Rb) == 0.09974296290198023
