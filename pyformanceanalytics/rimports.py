"""An interface to importing R packages."""
from __future__ import annotations

import functools

from rpy2 import robjects as ro

GGPLOT2_PACKAGE = "ggplot2"
GRIDEXTRA_PACKAGE = "gridExtra"
PERFORMANCE_ANALYTICS_PACKAGE = "PerformanceAnalytics"
GRDEVICES_PACKAGE = "grDevices"
UTILS_PACKAGE = "utils"
QUANTREG_PACKAGE = "quantreg"
PKG_PACKAGE = "pkg"

_IMPORTED_PACKAGES: dict[
    str, (ro.packages.InstalledSTPackage | ro.packages.InstalledPackage)  # type: ignore
] = {}


@functools.cache
def utils() -> ro.packages.InstalledSTPackage | ro.packages.InstalledPackage:  # type: ignore
    """Import the utils R package."""
    return ro.packages.importr("utils")  # type: ignore


def import_package(
    package: str,
) -> ro.packages.InstalledSTPackage | ro.packages.InstalledPackage:  # type: ignore
    """Import an R package to the global environment."""
    if package in _IMPORTED_PACKAGES:
        return _IMPORTED_PACKAGES[package]
    if not ro.packages.isinstalled(package):  # type: ignore
        utils().chooseCRANmirror(ind=1)
        utils().install_packages(ro.vectors.StrVector([package]))
    return ro.packages.importr(package)  # type: ignore


def ensure_packages_present(packages: list[str]):
    """Ensure that the list of R packages are present in the global environment."""
    for package in packages:
        import_package(package)
