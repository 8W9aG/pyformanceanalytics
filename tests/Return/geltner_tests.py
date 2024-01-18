"""Tests for the Geltner function."""
import pandas as pd
from pyformanceanalytics.Return import Geltner


def test_geltner():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    df = df[df.index.year == 1996]
    expected_df = pd.DataFrame(data={
        "HAM1": [None, 0.01876943580478983, 0.01566942386065535, -0.008003203428389059, 0.00685542671764623, -0.0033872698953851285, -0.022243963651425606, 0.036708964821835575, 0.015805713616908593, 0.02817134830651568, 0.016188524989644897, 0.017510829547023505],
    }, index=df.index)
    R = df[["HAM1"]]
    assert Geltner(R).to_csv() == expected_df.to_csv()
