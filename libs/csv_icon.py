import os
import cairosvg
import PIL.ImageOps
from PIL import Image
from io import BytesIO
from dataclasses import dataclass

from libs.shapes import Point
from libs.canvas import Canvas

RESOURCE_DIR = f"{os.getcwd()}/resource/icon/"


@dataclass
class EIcon:
    """
    resources must exist in "/resource/icon"
    """

    celsius: str = "wi-celsius.svg"
    cloud: str = "wi-cloud.svg"
    cloudy: str = "wi-cloudy.svg"
    day_cloudy: str = "wi-day-cloudy.svg"
    day_haze: str = "wi-day-haze.svg"
    day_sunny: str = "wi-day-sunny.svg"
    day_windy: str = "wi-day-windy.svg"
    na: str = "wi-na.svg"
    night_alt_cloudy: str = "wi-night-alt-cloudy.svg"
    night_clear: str = "wi-night-clear.svg"
    sandstorm: str = "wi-sandstorm.svg"
    snow: str = "wi-snow.svg"
    strong_wind: str = "wi-strong-wind.svg"
    sunrise: str = "wi-sunrise.svg"


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
