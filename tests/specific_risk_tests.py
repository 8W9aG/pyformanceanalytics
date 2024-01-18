"""Tests for the SpecificRisk function."""
import pandas as pd
from pyformanceanalytics import SpecificRisk


def test_specific_risk():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert SpecificRisk(Ra, Rb) == 0.06643961809120942
