"""Tests for the centeredcomoment function."""
import pandas as pd
from pyformanceanalytics import centeredcomoment


def test_centeredcomoment():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df[df.index.year == 1996]
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert centeredcomoment(Ra, Rb, 2.0, 2.0) == 3.905368496990161e-07
