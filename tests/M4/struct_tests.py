"""Tests for the struct function."""
import numpy as np
import pandas as pd
from pyformanceanalytics.M4 import struct


def test_struct():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_array = np.array([[
        2.278253e-06, 0.0, 0.0, float('nan'), 0.0, float('nan'), float('nan'), 0.0
    ], [
        0.0, float('nan'), float('nan'), 0.0, float('nan'), 0.0, 0.0, float('nan')
    ]])
    R = df[["HAM1", "HAM2"]]
    assert np.allclose(struct(R), expected_array, equal_nan=True)
