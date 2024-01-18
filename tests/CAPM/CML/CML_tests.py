"""Tests for the CML function."""
import pandas as pd
from pyformanceanalytics.CAPM.CML import CML


def test_CML():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert CML(Ra, Rb) == 0.00222544242959037
