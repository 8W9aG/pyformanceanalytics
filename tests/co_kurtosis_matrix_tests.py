"""Tests for the CoKurtosisMatrix function."""
import numpy as np
import pandas as pd
from pyformanceanalytics import CoKurtosisMatrix


def test_co_kurtosis_matrix():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_array = np.array([[2.278253e-06]])
    R = df[["HAM1"]]
    assert np.allclose(CoKurtosisMatrix(R), expected_array)
