"""Tests for the ProspectRatio function."""
import pandas as pd
from pyformanceanalytics import ProspectRatio


def test_prospect_ratio():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    R = df[["HAM1"]]
    assert ProspectRatio(R, 0.005) == 0.28870370562168857
