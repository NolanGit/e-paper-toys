import datetime

from libs.shapes import Point
from libs.canvas import Canvas
from libs.font import get_font
from libs.csv_icon import CsvIcon
from apps.weather.model.icon import EIcon
from libs.layout import Column, Row
from libs.line import Line
from libs.text import Text, TextAlign
from apps.weather.model.qweather_code_icon import QweatherCode

from apps.weather.service.data import (
    get_update_time,
    get_weather_by_date,
    get_aqi_by_date,
)
from apps.calendar.service.data import get_next_event, get_current_event
from apps.weather.draw import draw
from apps.const import WEEK_DICT, MONTH_DICT


canvas = Canvas(800, 480)
CURRENT_DATE = datetime.datetime.now(
    datetime.timezone(datetime.timedelta(hours=8), "zh")
)

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
calendar_col1 = calendar_row.add_col()
calendar_col2 = calendar_row.add_col()


current_event = get_current_event(
    CURRENT_DATE,
    "cn_zh.ics",
)

_text = f"{WEEK_DICT[CURRENT_DATE.weekday()]} {CURRENT_DATE.month}/{CURRENT_DATE.day}  {''.join(current_event)}"
Text(
    text=_text,
    font=get_font(),
    point=Point(x=calendar_col1.x, y=calendar_col1.center_point.y),
    canvas=canvas,
    align=TextAlign.Right,
).draw()
update_time = Text(
    text=f"Data update: {get_update_time()}",
    font=get_font(20),
    point=Point(x=calendar_col2.end_x, y=calendar_col2.center_point.y),
    canvas=canvas,
    align=TextAlign.Left,
).draw()


weather_row = Row(
    canvas=canvas,
    x=BASIC_X,
    y=calendar_row.end_y + 10,
    width=canvas.width - BASIC_X * 2,
    height=340,
)
draw(canvas=canvas, row=weather_row)

divider1 = Line(
    Point(BASIC_X, weather_row.end_y + 15),
    length=canvas.width - BASIC_X * 2,
    angle=0,
    width=1,
    canvas=canvas,
).draw()

buttom_col = Column(
    canvas=canvas,
    x=BASIC_X,
    y=weather_row.end_y + 10,
    width=canvas.width - BASIC_X * 2,
    height=canvas.height - STARTING_Y - weather_row.end_y,
)
next_event = get_next_event(
    CURRENT_DATE,
    "cn_zh.ics",
)
next_event_text = Text(
    text="",
    font=get_font(24),
    point=Point(BASIC_X, buttom_col.center_point.y),
    canvas=canvas,
    align=TextAlign.Right,
)
if next_event is not None:
    _diff = next_event.end.datetime - CURRENT_DATE
    next_event_text.text = f"{_diff.days} days to {next_event.name}"
next_event_text.draw()
print(next_event_text.length)
Line(
    Point(int(next_event_text.length) + BASIC_X + 10, divider1.start_point.y),
    length=buttom_col.height - 10,
    angle=-90,
    width=1,
    canvas=canvas,
).draw()

canvas.save("app.bmp")
