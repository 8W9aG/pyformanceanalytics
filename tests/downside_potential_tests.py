"""Tests for the DownsidePotential function."""
import pandas as pd
from pyformanceanalytics import DownsidePotential


def test_downside_potential():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    R = df[["HAM1"]]
    assert DownsidePotential(R) == 0.005077272727272728
