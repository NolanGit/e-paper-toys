from PIL import ImageDraw

from libs.canvas import Canvas
from libs.shapes import Point


class Basic(Canvas):
    x: int  # starting X coordinate
    y: int  # starting Y coordinate
    canvas: Canvas

    def rectangle_self(self, width=1):
        """
        draw a rectangle with self width and height
        """
        self.canvas.image_draw.rectangle(
            (
                self.x,
                self.y,
                self.x + self.width,
                self.y + self.height,
            ),
            outline=0,
            width=width,
        )

    @property
    def center_point(self) -> Point:
        return Point(self.x + self.width / 2, self.y + self.height / 2)


class Column(Basic):
    x = 0  # starting X coordinate
    y = 0  # starting Y coordinate
    width = 0
    height = 0
    margin_left = 0
    gutter = 0
    rows = []
    canvas: ImageDraw.ImageDraw = None
    width_fixed = False

    def __init__(self, canvas, x, y, width, height):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rows = []

    @property
    def end_x(self) -> int:
        """
        结束横坐标
        """
        return self.x + self.width

    def set_width(self, width):
        self.width = width
        self.width_fixed = True

    def add_row(self):
        """
        添加一列
        """
        row = Row(
            canvas=self.canvas,
            width=None,
            x=None,
            y=None,
            height=None,
        )
        self.rows.append(row)
        row.x = self.x
        row.width = self.width
        self._update_row()
        return row

    def _update_row(self):
        x = 0
        for row in self.rows:
            height_without_gutter = self.height - self.gutter * (len(self.rows) - 1)
            fixed_rows = [item for item in self.rows if item.height_fixed]
            height_without_fixed = height_without_gutter - sum([_.height for _ in fixed_rows])
            height_average = height_without_fixed/(len(self.rows)-len(fixed_rows))
            row.height = height_average if not row.height_fixed else row.height
            row.y = (
                self.y  # starting height
                + self.gutter * x  # 元素前面有几个gutter带来的高度
                + sum(
                    [item.height for item in self.rows[:x]]
                )  # 元素前面有几个元素height带来的高度
            )
            x += 1


class Row(Basic):
    x = 0  # starting X coordinate
    y = 0  # 起始纵坐标
    width = 0  # 总宽度
    height = 0  # 总高度
    gutter = 0
    columns = []
    canvas: ImageDraw.ImageDraw = None
    height_fixed = False

    def __init__(self, canvas, x, y, width, height):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.columns = []

    @property
    def end_y(self) -> int:
        """
        结束纵坐标
        """
        return self.y + self.height

    def set_height(self, height):
        self.height = height
        self.height_fixed = True

    def add_col(self):
        """
        添加一列
        """
        col = Column(
            canvas=self.canvas,
            width=None,
            x=None,
            y=None,
            height=None,
        )
        self.columns.append(col)
        col.y = self.y
        col.height = self.height
        self._update_col()
        return col

    def _update_col(self):
        x = 0
        for col in self.columns:
            width_without_gutter = self.width - self.gutter * (len(self.columns) - 1)
            fixed_cols = [item for item in self.columns if item.width_fixed]
            width_without_fixed = width_without_gutter - sum([_.width for _ in fixed_cols])
            width_average = width_without_fixed/(len(self.columns)-len(fixed_cols))
            col.width = width_average if not col.width_fixed else col.width
            col.x = (
                self.x  # starting width
                + self.gutter * x  # 元素前面有几个gutter带来的宽度
                + sum(
                    [item.width for item in self.columns[:x]]
                )  # 元素前面有几个元素width带来的宽度
            )
            x += 1
