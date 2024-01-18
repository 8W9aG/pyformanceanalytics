"""Tests for the UpsideRisk function."""
import pandas as pd
from pyformanceanalytics import UpsideRisk


def test_upside_risk():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    R = df[["HAM1"]]
    assert UpsideRisk(R) == 0.027565610044815926
