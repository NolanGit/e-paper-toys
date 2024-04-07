from libs.canvas import Canvas
from libs.shapes import Point


class ProcessBar:
    start_point: Point
    width: int
    height: int
    process: float
    canvas: Canvas
    padding: int = 2

    def __init__(
        self,
        start_point: Point,
        width: int,
        height: int,
        process: float,
        canvas: Canvas,
    ) -> None:
        self.x = start_point.x
        self.y = start_point.y
        self.width = width
        self.height = height
        self.process = process
        self.canvas = canvas

    def draw(self):
        self.canvas.image_draw.rectangle(
            (
                self.x,
                self.y,
                self.x + self.width,
                self.y + self.height,
            ),
            outline=0,
            width=1,
        )
        self.process_end_x = int(self.process * (self.width - 2 * self.padding))
        self.canvas.image_draw.rectangle(
            (
                self.x + self.padding,
                self.y + self.padding,
                self.x + self.process_end_x,
                self.y + self.height - 2 * self.padding,
            ),
            outline=0,
            fill=1,
            width=1,
        )
