"""Tests for the MM function."""
import numpy as np
import pandas as pd
from pyformanceanalytics.M3 import MM


def test_MM():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_array = np.array([[-1.12188262e-05]])
    R = df[["HAM1"]]
    assert np.allclose(MM(R), expected_array)
