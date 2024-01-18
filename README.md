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

- [PerformanceAnalytics 2.0.4](https://github.com/braverock/PerformanceAnalytics)
- [ggplot2 3.4.4](https://ggplot2.tidyverse.org/)
- [gridExtra 2.3](https://cran.r-project.org/web/packages/gridExtra/index.html)
- [quantreg 5.97](https://www.rdocumentation.org/packages/quantreg/versions/5.97)
- [RobStatTM 1.0.8](https://github.com/msalibian/RobStatTM)

## Raison D'être :thought_balloon:

PerformanceAnalytics is an outstanding Econometrics library written in R that has been battle tested by many quantitative finance firms.
We have a need to use this alongside some machine learning we are doing in python, so to bridge the gap we created this wrapper library.
The library very closely follows the conventions laid out in PerformanceAnalytics, for example to determine information ratio you can simply use the following code:

```python
from pyformanceanalytics import InformationRatio

inf_rat_flt = InformationRatio(df)
```

The functions and modules are designed to be as close to the PerformanceAnalytics package as possible for easy porting.


## Installation :inbox_tray:

This is a python package hosted on pypi, so to install simply run the following command:

`pip install pyformanceanalytics`

Note that upon running this package for the first time, you may notice a slight delay as it downloads the relevant R packages.

## Usage example :eyes:

To get familiar with the individual functions and charts check out the documents in the [pyformanceanalytics README](pyformanceanalytics/README.md). This library ports over 100 functions, 20 charts and 20 tables.

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

You can feed in multiple portfolios to get your results in a `DataFrame`, else they may be reported as single floats.

## License :memo:

The project is available under the [GPL2 License](LICENSE).
