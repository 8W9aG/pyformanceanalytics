# pyformanceanalytics.RPESE

These examples will draw on the following datasets:

```python
import pandas as pd

df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
df.index = pd.to_datetime(df.index)
weights_df = pd.read_csv("pyformanceanalytics/weights.csv", index_col=0)
```

## Functions

The following functions are supported:

### control

Control sets the different control parameters used in the compuation of standard errors for
risk and performance estimators

```python
from pyformanceanalytics.RPESE import control

control()
```
