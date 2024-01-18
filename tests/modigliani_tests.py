"""Tests for the Modigliani function."""
import pandas as pd
from pyformanceanalytics import Modigliani


def test_modigliani():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert Modigliani(Ra, Rb) == 0.018795914187992774
