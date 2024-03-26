import cairosvg
import PIL.ImageOps
from PIL import Image
from io import BytesIO
from dataclasses import dataclass

from libs.canvas import Canvas


@dataclass
class EIcon:
    celsius: str = "wi-celsius.svg"
    cloud: str = "wi-cloud.svg"
    cloudy: str = "wi-cloudy.svg"
    day_cloudy: str = "wi-day-cloudy.svg"
    day_haze: str = "wi-day-haze.svg"
    day_sunny: str = "wi-day-sunny.svg"
    day_windy: str = "wi-day-windy.svg"
    na: str = "wi-na.svg"


class CsvIcon:
    canvas: Canvas
    icon: EIcon

    def draw(self):
        out = BytesIO()
        cairosvg.svg2png(
            url="/workspaces/e-paper-toys/wi-cloud.svg", scale=10, write_to=out
        )
        image = Image.open(out)
        _, _, _, a = image.split()
        a = PIL.ImageOps.invert(a)
        self.canvas.Limage.paste(a)
