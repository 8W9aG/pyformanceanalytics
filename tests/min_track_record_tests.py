"""Tests for the MinTrackRecord function."""
import pandas as pd
from pyformanceanalytics import MinTrackRecord


def test_min_track_record():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "HAM1..SR...0.23..": [72.13939047185043],
        "IS_SR_SIGNIFICANT": [True],
        "num_of_extra_obs_needed": [0.0],
    }, index=["Minimum Track Record Length (p= 95 %):"])
    R = df[["HAM1"]]
    assert MinTrackRecord(0.23, R=R).equals(expected_df)
