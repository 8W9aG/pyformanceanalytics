"""Functions for converting a ggplot to a python image."""
import tempfile
from typing import Any

from PIL import Image
from rpy2 import robjects


def ggplot_to_image(plot: Any) -> Image:
    """Render an R ggplot to an image."""
    with tempfile.NamedTemporaryFile(suffix=".png") as temp_handle:
        path = temp_handle.name
        temp_handle.close()
        robjects.r("ggsave").rcall(
            (
                ("file", path),
                ("plot", plot),
            ),
        )
        return Image.open(path)
