"""Functions for converting a ggplot to a python image."""
import tempfile
from typing import Any

from PIL import Image
from rpy2 import robjects as ro

DPI = 300.0


def ggplot_to_image(plot: Any, width: int, height: int) -> Image.Image:
    """Render an R ggplot to an image."""
    with tempfile.NamedTemporaryFile(suffix=".png") as temp_handle:
        path = temp_handle.name
        temp_handle.close()
        ro.r("ggsave").rcall(  # type: ignore
            (
                ("file", path),
                ("plot", plot),
                ("width", (float(width) / DPI) * 4.0),
                ("height", (float(height) / DPI) * 4.0),
                ("dpi", DPI),
            ),
        )
        return Image.open(path)
