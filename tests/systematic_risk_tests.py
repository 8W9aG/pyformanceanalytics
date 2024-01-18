"""Tests for the SystematicRisk function."""
import pandas as pd
from pyformanceanalytics import SystematicRisk


def test_systematic_risk():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert SystematicRisk(Ra, Rb) == 0.05860128475653231
