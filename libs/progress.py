from libs.canvas import Canvas
from libs.shapes import Point


class ProgressBar:
    start_point: Point
    width: int
    height: int
    progress: float
    canvas: Canvas
    padding: int = 2

    def __init__(
        self,
        start_point: Point,
        width: int,
        height: int,
        progress: float,
        canvas: Canvas,
        padding: int = 2,
    ) -> None:
        self.x = start_point.x
        self.y = start_point.y
        self.width = width
        self.height = height
        self.progress = progress
        self.canvas = canvas
        self.padding = padding

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
        self.progress_end_x = int(self.progress * (self.width - 2 * self.padding))
        self.canvas.image_draw.rectangle(
            xy=[
                (self.x + self.padding, self.y + self.padding),
                (
                    self.x + self.progress_end_x,
                    self.y + self.height -  self.padding,
                ),
            ],
            width=int(self.height/2),
        )
