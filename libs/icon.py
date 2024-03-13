from libs.canvas import Canvas
from libs.shapes import Point
from libs.line import Line

from PIL import ImageFont


class IconSun:
    center_point: Point
    canvas: Canvas

    def __init__(
        self,
        center_point: Point,
        canvas: Canvas,
        size: int,
        line_width: int,
        lines_count: int,
    ):
        self.center_point = center_point
        self.canvas = canvas
        self.size = size
        self.line_width = line_width
        self.lines_count = lines_count

    def draw(self):
        self._draw_circle()
        self._draw_lines()

    def _draw_circle(self):
        self.canvas.image_draw.arc(
            (
                self.center_point.x - self.size / 2,
                self.center_point.y - self.size / 2,
                self.center_point.x + self.size / 2,
                self.center_point.y + self.size / 2,
            ),
            start=0,
            end=360,
            fill=0,
            width=self.line_width,
        )

    def _draw_lines(self):
        for x in range(self.lines_count):
            _temp_line = Line(
                start_point=self.center_point,
                length=self.size * 0.7,
                angle=x * 360 / self.lines_count,
                line_width=self.line_width,
                canvas=self.canvas,
            )
            Line(
                start_point=Point(x=_temp_line.end_point.x, y=_temp_line.end_point.y),
                length=self.size / 3,
                angle=x * 360 / self.lines_count,
                line_width=self.line_width,
                canvas=self.canvas,
            ).draw()
