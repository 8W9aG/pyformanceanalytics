# pyformanceanalytics.mean

These examples will draw on the following datasets:

```python
import pandas as pd

df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
df.index = pd.to_datetime(df.index)
weights_df = pd.read_csv("pyformanceanalytics/weights.csv", index_col=0)
```

## Functions

The following functions are supported:

### geometric

Calculate the geometric mean

```python
from pyformanceanalytics.mean import geometric

R = df[["HAM1"]]
geometric(R)
```

### stderr

Calculate the standard error of the mean

```python
from pyformanceanalytics.mean import stderr

R = df[["HAM1"]]
stderr(R)
```

### LCL

Calculate the lower confidence level of the mean

```python
from pyformanceanalytics.mean import LCL

R = df[["HAM1"]]
LCL(R)
```

### UCL

Calculate the upper confidence level of the mean

```python
from pyformanceanalytics.mean import UCL

R = df[["HAM1"]]
UCL(R)
```
