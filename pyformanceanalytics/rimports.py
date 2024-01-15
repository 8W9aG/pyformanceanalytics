"""An interface to importing R packages."""
import functools
from typing import Any, Dict, List

import rpy2.robjects.packages as rpackages
from rpy2.robjects.vectors import StrVector


GGPLOT2_PACKAGE = "ggplot2"
GRIDEXTRA_PACKAGE = "gridExtra"
PERFORMANCE_ANALYTICS_PACKAGE = "PerformanceAnalytics"
GRDEVICES_PACKAGE = "grDevices"
UTILS_PACKAGE = "utils"
QUANTREG_PACKAGE = "quantreg"
PKG_PACKAGE = "pkg"

_IMPORTED_PACKAGES: Dict[str, Any] = {}


@functools.cache
def utils() -> Any:
    """Import the utils R package."""
    return rpackages.importr("utils")


def import_package(package: str) -> Any:
    """Import an R package to the global environment."""
    global _IMPORTED_PACKAGES
    if package in _IMPORTED_PACKAGES:
        return _IMPORTED_PACKAGES[package]
    if not rpackages.isinstalled(package):
        utils().chooseCRANmirror(ind=1)
        utils().install_packages(StrVector([package]))
    return rpackages.importr(package)


def ensure_packages_present(packages: List[str]):
    """Ensure that the list of R packages are present in the global environment."""
    for package in packages:
        import_package(package)
