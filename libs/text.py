from dataclasses import dataclass
from libs.canvas import Canvas
from libs.shapes import Point

from PIL import ImageFont


@dataclass
class TextAlign:
    Center: str = "center"
    Left: str = "left"
    Right: str = "right"


class Text:
    """
    write a text on canvas, align center
    """

    point: Point
    canvas: Canvas
    font: ImageFont

    def __init__(
        self,
        text,
        font,
        point,
        canvas,
        align: str = TextAlign.Center,
        x_delta=0,
        y_delta=0,
    ):
        self.text = text
        self.font = font
        self.point = point
        self.canvas = canvas
        self.align = align
        self.x_delta = x_delta
        self.y_delta = y_delta
        self._cal_length()

    def _cal_length(self):
        self.length = self.canvas.image_draw.textlength(text=self.text, font=self.font)

    @property
    def x(self):
        """
        text starting X coordinate
        """
        if self.align == TextAlign.Center:
            return self.point.x - self.length / 2 + self.x_delta
        elif self.align == TextAlign.Left:
            return self.point.x -self.length+ self.x_delta
        elif self.align == TextAlign.Right:
            return self.point.x + self.x_delta

    @property
    def y(self):
        """
        text starting Y coordinate
        """
        return (
            self.point.y - self.font.size * (2 / 3) + self.y_delta
        )  # I don't know why size*(2/3) seems perfect

    def draw(self):
        self.canvas.image_draw.text(xy=(self.x, self.y), text=self.text, font=self.font)
