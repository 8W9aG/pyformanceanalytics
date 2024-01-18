"""Tests for the CoSkewnessMatrix function."""
import numpy as np
import pandas as pd
from pyformanceanalytics import CoSkewnessMatrix


def test_co_skewness_matrix():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_array = np.array([[-1.09651406e-05]])
    R = df[["HAM1"]]
    assert np.allclose(CoSkewnessMatrix(R), expected_array)
