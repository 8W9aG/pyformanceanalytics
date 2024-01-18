"""Tests for the jensenAlpha function."""
import pandas as pd
from pyformanceanalytics.CAPM import jensenAlpha


def test_jensen_alpha():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df[df.index.year == 1996]
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert jensenAlpha(Ra, Rb) == 0.0807787061836887
