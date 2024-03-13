import math

from libs.canvas import Canvas
from libs.shapes import Point


class Line:
    start_point: Point
    end_point: Point
    canvas: Canvas

    def __init__(self, start_point: Point, length: int, angle: int,line_width:int, canvas: Canvas):
        self.start_point = start_point
        self.length = length
        self.angle = angle
        self.line_width = line_width
        _ = Point(
            self.start_point.x + math.cos(math.radians(self.angle)) * self.length,
            self.start_point.y - math.sin(math.radians(self.angle)) * self.length,
        )
        self.end_point = _
        self.canvas = canvas

    def draw(self):
        self.canvas.image_draw.line(
            (
                self.start_point.x,
                self.start_point.y,
                self.end_point.x,
                self.end_point.y,
            ),
            fill=0,
            width=self.line_width
        )
