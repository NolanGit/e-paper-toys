import datetime

from libs.shapes import Point
from libs.canvas import Canvas
from libs.font import get_font
from libs.layout import Column, Row
from libs.progress import ProgressBar
from libs.line import Line
from libs.text import Text, TextAlign

from apps.weather.service.data import (
    get_update_time,
)
from apps.calendar.service.data import get_next_event, get_current_event
from apps.weather.draw import draw
from apps.const import WEEK_DICT, MONTH_DICT


canvas = Canvas(800, 480)
CURRENT_DATE = datetime.datetime.now(
    datetime.timezone(datetime.timedelta(hours=8), "zh")
)

BASIC_X_MARGIN = 15
BASIC_Y_MARGIN = 15
CALENDAR_ROW_HEIGHT = 20

calendar_row = Row(
    canvas=canvas,
    x=0,
    y=0,
    width=canvas.width - BASIC_X_MARGIN * 2,
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
    x=BASIC_X_MARGIN,
    y=calendar_row.end_y + 10,
    width=canvas.width - BASIC_X_MARGIN * 2,
    height=340,
)
draw(canvas=canvas, row=weather_row)

divider1 = Line(
    Point(0, weather_row.end_y + BASIC_Y_MARGIN),
    length=canvas.width,
    angle=0,
    width=1,
    canvas=canvas,
).draw()

bottom_row = Row(
    canvas=canvas,
    x=BASIC_X_MARGIN,
    y=weather_row.end_y + BASIC_Y_MARGIN,
    width=canvas.width,
    height=canvas.height - BASIC_Y_MARGIN - weather_row.end_y,
)

next_event = get_next_event(
    CURRENT_DATE,
    "cn_zh.ics",
)
next_event_text = Text(
    text="",
    font=get_font(24),
    point=Point(0, bottom_row.center_point.y),
    canvas=canvas,
    align=TextAlign.Right,
)
if next_event is not None:
    _diff = next_event.end.datetime - CURRENT_DATE
    next_event_text.text = f"{_diff.days} days to {next_event.name}"
next_event_text.draw()

next_event_col = bottom_row.add_col()
next_event_col.set_width(next_event_text.length + BASIC_X_MARGIN)
progress_col = bottom_row.add_col()

divider2 = Line(
    Point(int(next_event_text.length) + BASIC_X_MARGIN, divider1.start_point.y),
    length=bottom_row.height,
    angle=-90,
    width=1,
    canvas=canvas,
).draw()

progress_text_row = progress_col.add_row()
progress_bar_row = progress_col.add_row()
_progress = (
    CURRENT_DATE
    - datetime.datetime(CURRENT_DATE.year, 1, 1, tzinfo=datetime.timezone.utc)
).days / 365
Text(
    text=f"{CURRENT_DATE.year} is {format(_progress*100,'.3f')} % complete.",
    font=get_font(24),
    point=progress_text_row.center_point,
    canvas=canvas,
    align=TextAlign.Center,
).draw()
ProgressBar(
    start_point=Point(
        divider2.start_point.x + BASIC_X_MARGIN,
        progress_text_row.end_y,
    ),
    width=canvas.width - 2 * BASIC_Y_MARGIN - divider2.start_point.x,
    height=progress_bar_row.height - BASIC_Y_MARGIN,
    progress=_progress,
    canvas=canvas,
    padding=5,
).draw()

canvas.save("app.bmp")
