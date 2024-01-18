"""An interface to importing R packages."""
from __future__ import annotations

import functools

import rpy2.robjects.packages as rpackages
from rpy2 import robjects as ro

GGPLOT2_PACKAGE = "ggplot2"
GRIDEXTRA_PACKAGE = "gridExtra"
PERFORMANCE_ANALYTICS_PACKAGE = "PerformanceAnalytics"
GRDEVICES_PACKAGE = "grDevices"
UTILS_PACKAGE = "utils"
QUANTREG_PACKAGE = "quantreg"
ROB_STAT_TM_PACKAGE = "RobStatTM"

_IMPORTED_PACKAGES: dict[
    str, (rpackages.InstalledSTPackage | rpackages.InstalledPackage)  # type: ignore
] = {}
_VERSIONED_PACKAGES = {
    GGPLOT2_PACKAGE: "https://cran.r-project.org/src/contrib/ggplot2_3.4.4.tar.gz",
    GRIDEXTRA_PACKAGE: "https://cran.r-project.org/src/contrib/gridExtra_2.3.tar.gz",
}


@functools.cache
def utils() -> rpackages.InstalledSTPackage | rpackages.InstalledPackage:  # type: ignore
    """Import the utils R package."""
    return rpackages.importr("utils")  # type: ignore


def import_package(
    package: str,
) -> rpackages.InstalledSTPackage | rpackages.InstalledPackage:  # type: ignore
    """Import an R package to the global environment."""
    if package in _IMPORTED_PACKAGES:
        return _IMPORTED_PACKAGES[package]
    if not rpackages.isinstalled(package):  # type: ignore
        utils().chooseCRANmirror(ind=1)
        utils().install_packages(
            ro.vectors.StrVector([_VERSIONED_PACKAGES.get(package, package)])
        )
    return rpackages.importr(package)  # type: ignore


def ensure_packages_present(packages: list[str]):
    """Ensure that the list of R packages are present in the global environment."""
    for package in packages:
        import_package(package)
