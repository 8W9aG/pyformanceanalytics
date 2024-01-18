"""Functions for converting a plot to a python image."""
import tempfile
from collections.abc import Callable

from PIL import Image
from rpy2 import robjects as ro

from .rimports import GRDEVICES_PACKAGE, import_package


def plot_to_image(
    plot_func: Callable[[], None], width: int, height: int
) -> Image.Image:
    """Render an R plot to an image."""
    with tempfile.NamedTemporaryFile(suffix=".png") as temp_handle:
        path = temp_handle.name
        temp_handle.close()
        grdevices = import_package(GRDEVICES_PACKAGE)
        grdevices.png(file=temp_handle.name, width=width, height=height)
        plot_func()
        grdevices.dev_off()
        return Image.open(path)


def plot_ro(x: ro.RObject, env: ro.Environment) -> ro.RObject:
    return ro.r("plot").rcall(  # type: ignore
        (
            (
                "x",
                x,
            ),
        ),
        env,
    )
