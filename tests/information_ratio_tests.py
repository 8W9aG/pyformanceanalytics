"""Tests for the InformationRatio function."""
import pandas as pd
from pyformanceanalytics import InformationRatio


def test_information_ratio():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert InformationRatio(Ra, Rb) == 0.36041251297991556
