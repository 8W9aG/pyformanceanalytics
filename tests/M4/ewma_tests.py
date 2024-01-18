"""Tests for the ewma function."""
import numpy as np
import pandas as pd
from pyformanceanalytics.M4 import ewma


def test_ewma():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_array = np.array([[1.856763e-06]])
    R = df[["HAM1"]]
    assert np.allclose(ewma(R), expected_array)
