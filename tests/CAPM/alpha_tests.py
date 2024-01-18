"""Tests for the alpha function."""
import pandas as pd
from pyformanceanalytics.CAPM import alpha


def test_alpha():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    Ra = df[["HAM1"]]
    Rb = df[["SP500 TR"]]
    assert alpha(Ra, Rb) == 0.0077380162961344
