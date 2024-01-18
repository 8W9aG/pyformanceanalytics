# pyformanceanalytics.StdDev

These examples will draw on the following datasets:

```python
import pandas as pd

df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
df.index = pd.to_datetime(df.index)
weights_df = pd.read_csv("pyformanceanalytics/weights.csv", index_col=0)
```

## Functions

The following functions are supported:

### StdDev

Calculates Standard Deviation for univariate and multivariate series, also calculates component con-
tribution to standard deviation of a portfolio.

```python
from pyformanceanalytics.StdDev import StdDev

R = df[["HAM1"]]
StdDev(R)
```

### annualized

Calculate a multiperiod or annualized Standard Deviation

```python
from pyformanceanalytics.StdDev import annualized

R = df[["HAM1"]]
annualized(R)
```
