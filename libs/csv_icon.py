import os
import cairosvg
import PIL.ImageOps
from PIL import Image
from io import BytesIO

from libs.shapes import Point
from libs.canvas import Canvas
from apps.weather.model.icon import EIcon




class CsvIcon:
    canvas: Canvas
    icon: EIcon
    center_point: Point

    def __init__(
        self, icon: EIcon, canvas: Canvas, center_point: Point, size: int
    ) -> None:
        self.icon = icon
        self.canvas = canvas
        self.center_point = center_point
        self.size = size

    def draw(self):
        _out = BytesIO()
        cairosvg.svg2png(url=f"{RESOURCE_DIR}{self.icon}", scale=10, write_to=_out)
        _image = Image.open(_out)
        _, _, _, a = _image.split()
        a = PIL.ImageOps.invert(a)  # invert icon color from white to black
        a = a.resize((self.size, self.size))
        self.canvas.Limage.paste(
            a,
            (int(self.center_point.x - self.size/2), int(self.center_point.y - self.size/2)),
        )

s