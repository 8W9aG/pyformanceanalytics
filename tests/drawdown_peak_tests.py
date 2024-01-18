"""Tests for the DrawdownPeak function."""
import numpy as np
import pandas as pd
from pyformanceanalytics import DrawdownPeak


def test_drawdown_peak():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df[df.index.year == 1996]
    expected_array = np.array([[0.0, 0.0, 0.0, -0.009100, -0.00150069, -0.00540063, -0.02849939, 0.0, 0.0, 0.0, 0.0, 0.0]])
    R = df[["HAM1"]]
    assert np.allclose(DrawdownPeak(R), expected_array)
