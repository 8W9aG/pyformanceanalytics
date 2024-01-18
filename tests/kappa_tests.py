"""Tests for the Kappa function."""
import pandas as pd
from pyformanceanalytics import Kappa


def test_kappa():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    R = df[["HAM1"]]
    assert Kappa(R, 0.005, 2) == 0.37305993266200166
