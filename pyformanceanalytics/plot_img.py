"""Functions for converting a plot to a python image."""
import tempfile
from typing import Any, Callable

from PIL import Image
from rpy2 import robjects

from .rimports import import_package, GRDEVICES_PACKAGE


def plot_to_image(plot_func: Callable[[], None]) -> Image:
    """Render an R plot to an image."""
    with tempfile.NamedTemporaryFile(suffix=".png") as temp_handle:
        path = temp_handle.name
        temp_handle.close()
        grdevices = import_package(GRDEVICES_PACKAGE)
        grdevices.png(file=temp_handle.name, width=512, height=512)
        plot_func()
        grdevices.dev_off()
        return Image.open(path)
