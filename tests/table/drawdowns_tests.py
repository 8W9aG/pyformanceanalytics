"""Tests for the Drawdowns function."""
import pandas as pd
from pyformanceanalytics.table import Drawdowns

def test_drawdowns():
    df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
    df.index = pd.to_datetime(df.index)
    expected_df = pd.DataFrame(data={
        "From": ["2002-02-28 00:00:00-05:00", "1998-05-31 00:00:00-04:00", "2005-03-31 00:00:00-05:00", "2001-09-30 00:00:00-04:00", "1996-04-30 00:00:00-04:00"],
        "Trough": ["2003-02-28 00:00:00-05:00", "1998-08-31 00:00:00-04:00", "2005-04-30 00:00:00-04:00", "2001-09-30 00:00:00-04:00", "1996-07-31 00:00:00-04:00"],
        "To": ["2003-07-31 00:00:00-04:00", "1999-03-31 00:00:00-05:00", "2005-09-30 00:00:00-04:00", "2001-11-30 00:00:00-05:00", "1996-08-31 00:00:00-04:00"],
        "Depth": [-0.1518, -0.1239, -0.0412, -0.0312, -0.0284],
        "Length": [18.0, 11.0, 7.0, 3.0, 5.0],
        "To Trough": [13.0, 4.0, 2.0, 1.0, 4.0],
        "Recovery": [5.0, 7.0, 5.0, 2.0, 1.0],
    }, index=[1, 2, 3, 4, 5])
    R = df[["HAM1"]]
    assert Drawdowns(R).to_csv() == expected_df.to_csv()
