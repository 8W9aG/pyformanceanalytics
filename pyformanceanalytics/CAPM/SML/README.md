# pyformanceanalytics.CAPM.SML

These examples will draw on the following datasets:

```python
import pandas as pd

df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
df.index = pd.to_datetime(df.index)
weights_df = pd.read_csv("pyformanceanalytics/weights.csv", index_col=0)
```

## Functions

The following functions are supported:

### slope

The slope of the Security Market Line

```python
from pyformanceanalytics.CAPM.SML import slope

R = df[["SP500 TR"]]
slope(R)
```
