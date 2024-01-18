# pyformanceanalytics

<a href="https://pypi.org/project/pyformance-analytics/">
    <img alt="PyPi" src="https://img.shields.io/pypi/v/pyformance-analytics">
</a>

A python wrapper around the Econometrics [PerformanceAnalytics R package](https://github.com/braverock/PerformanceAnalytics).

## Dependencies :globe_with_meridians:

Python 3.11.6:

- [rpy2 3.5.15](https://rpy2.github.io/)
- [pandas 2.1.4](https://pandas.pydata.org/)
- [Pillow 10.2.0](https://pillow.readthedocs.io/en/stable/reference/Image.html)
- [numpy 1.26.3](https://numpy.org/)

R 4.3.2:

- [PerformanceAnalytics](https://github.com/braverock/PerformanceAnalytics)
- [ggplot2](https://ggplot2.tidyverse.org/)
- [gridExtra](https://cran.r-project.org/web/packages/gridExtra/index.html)

## Installation :inbox_tray:

This is a python package hosted on pypi, so to install simply run the following command:

`pip install pyformance-analytics`

## Usage example :eyes:

To get familiar with the individual functions and charts check out the documents in the [pyformanceanalytics README](pyformanceanalytics/README.md).

This supports both tables, functions and charts. An example of generating a chart:

```python
import pandas as pd
from pyformanceanalytics.charts import PerformanceSummary

df = pd.read_csv("pyformanceanalytics/managers.csv", index_col=0)
df.index = pd.to_datetime(df.index)
PerformanceSummary(df).show()
```

![PerformanceSummary](pyformanceanalytics/charts/PerformanceSummary.jpg "PerformanceSummary")

This outputs a `PIL` image, which automatically shows on colab instances.

## License :memo:

The project is available under the [GPL2 License](LICENSE).
