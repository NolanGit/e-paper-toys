import datetime

from libs.canvas import Canvas
from libs.layout import Column, Row
from libs.shapes import Point
from libs.text import Text, TextAlign
from libs.icon import IconSun,IconCloud,IconRain,IconSnow
from libs.line import Line
from libs.font import font24

canvas = Canvas(800, 480)

BORDER_WIDTH = 5
border = Row(canvas=canvas, x=0, y=0, width=canvas.width, height=canvas.height)
border.rectangle_self(BORDER_WIDTH)

BASIC_X = 15
STARTING_Y = 15
CALENDAR_ROW_HEIGHT = 20

calendar_row = Row(
    canvas=canvas,
    x=BASIC_X,
    y=STARTING_Y,
    width=canvas.width - BASIC_X * 2,
    height=CALENDAR_ROW_HEIGHT,
)
calendar_row.rectangle_self()
week_dict = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

_text = f"{week_dict[datetime.datetime.now().weekday()]} {datetime.datetime.now().month}/{datetime.datetime.now().day}"
Text(
    text=_text,
    font=font24,
    point=Point(x=calendar_row.x, y=calendar_row.center_point.y),
    canvas=canvas,
    align=TextAlign.Left,
).draw()


col = Column(
    canvas=canvas,
    x=BASIC_X,
    y=calendar_row.end_y + 10,
    width=canvas.width - BASIC_X * 2,
    height=canvas.height - 2 * BORDER_WIDTH - STARTING_Y - calendar_row.end_y,
)
col.gutter = 10
row1 = col.add_row()
row1.set_height(20)
row2 = col.add_row()

row1.gutter = 10
row1_col1 = row1.add_col()
row1_col2 = row1.add_col()
row1_col3 = row1.add_col()
row1_col4 = row1.add_col()
row1_col1.rectangle_self()
row1_col4.rectangle_self()

IconSun(center_point=row1_col4.center_point, canvas=canvas, size=30, width=5, lines_count=7).draw()
IconCloud(center_point=row1_col3.center_point, canvas=canvas, size=30, width=5).draw()
IconRain(center_point=row1_col2.center_point, canvas=canvas, size=30, width=5).draw()
IconSnow(center_point=row1_col1.center_point, canvas=canvas, size=30, width=5).draw()

row2.gutter = 30
row2_col1 = row2.add_col()
row2_col2 = row2.add_col()
row2_col3 = row2.add_col()
row2_col1.rectangle_self()
row2_col2.rectangle_self()
row2_col3.rectangle_self()


text = Text("hello", font24, Point(row2.center_point.x, row2.center_point.y), canvas)
text.draw()
print(123)
canvas.save("weather.bmp")
