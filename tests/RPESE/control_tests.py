"""Tests for the control function."""
import pandas as pd
from pyformanceanalytics.RPESE import control, ControlEstimator


def test_control():
    expected_df = pd.DataFrame(data={
        "se.method": ["IFiid", "IFcorAdapt"],
        "cleanOutliers": [False, False],
        "fitting.method": ["Exponential", "Exponential"],
        "freq.include": ["All", "All"],
        "freq.par": [0.5, 0.5],
        "a": [0.3, 0.3],
        "b": [0.7, 0.7],
    }, index=[1, 2])
    assert control(ControlEstimator.MEAN).to_csv() == expected_df.to_csv()
