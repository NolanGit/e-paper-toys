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

WEEK_DICT = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

MONTH_DICT = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}


def fill_detail_area(col: Column, canvas: Canvas, date: datetime.datetime):
    temperature_range_area = col.add_row()
    text_area = col.add_row()
    wind_area = col.add_row()
    sunrise_area = col.add_row()
    sunrise_area_icon = sunrise_area.add_col()
    sunrise_area_text = sunrise_area.add_col()
    weather = get_weather_by_date(date=date)
    aqi = get_aqi_by_date(date=date)
    Text(
        text=f"{weather.tempMin} ~ {weather.tempMax}°C",
        font=get_font(27),
        point=temperature_range_area.center_point,
        canvas=canvas,
        align=TextAlign.Center,
    ).draw()
    Text(
        text=f"{weather.textDay} to {weather.textNight}",
        font=get_font(18),
        point=text_area.center_point,
        canvas=canvas,
        align=TextAlign.Center,
    ).draw()
    Text(
        text=f"{aqi.category}",
        font=get_font(18),
        point=wind_area.center_point,
        canvas=canvas,
        align=TextAlign.Center,
        text_type="primary",
    ).draw()
    CsvIcon(
        icon=EIcon.sunrise,
        canvas=canvas,
        center_point=sunrise_area_icon.center_point,
        size=29,
    ).draw()
    Text(
        text=f"{weather.sunrise}",
        font=get_font(20),
        point=sunrise_area_text.center_point,
        canvas=canvas,
        align=TextAlign.Center,
        x_delta=-25,
    ).draw()


def fill_today_content(col: Column, canvas: Canvas):
    icon_area = col.add_row()
    temperature_area = col.add_row()
    temperature_area_number = temperature_area.add_col()
    _ = temperature_area.add_col()
    degree_area = _.add_row()
    text_area = _.add_row()
    weather = get_weather_by_date(date=datetime.datetime.now())
    _icon = QweatherCode(weather.iconDay).icon
    CsvIcon(
        icon=_icon,
        canvas=canvas,
        center_point=Point(icon_area.center_point.x, icon_area.center_point.y + 10),
        size=140,
    ).draw()

    Text(
        text=f"{weather.tempMax}",
        font=get_font(60),
        point=Point(
            temperature_area_number.end_x, temperature_area_number.center_point.y
        ),
        canvas=canvas,
        align=TextAlign.Left,
    ).draw()

    Text(
        text="°C",
        font=get_font(30),
        point=degree_area.center_point,
        canvas=canvas,
        align=TextAlign.Left,
        y_delta=10,
    ).draw()

    Text(
        text=f"{weather.textDay}",
        font=get_font(24),
        point=Point(text_area.center_point.x, text_area.center_point.y),
        canvas=canvas,
        align=TextAlign.Center,
        y_delta=-15,
        x_delta=5,
    ).draw()


def fill_next_days_content(col: Column, canvas: Canvas, date: datetime.datetime):
    week_area = col.add_row()
    week_area.set_height(45)
    date_area = col.add_row()
    date_area.set_height(38)
    icon_area = col.add_row()
    icon_area.set_height(130)
    weather = get_weather_by_date(date=date)
    _icon = QweatherCode(weather.iconDay).icon
    CsvIcon(
        icon=_icon,
        canvas=canvas,
        center_point=icon_area.center_point,
        size=120,
    ).draw()
    Text(
        text=f"{WEEK_DICT[date.weekday()]} ",
        font=get_font(20),
        point=week_area.center_point,
        canvas=canvas,
        align=TextAlign.Center,
        y_delta=10,
    ).draw()
    Text(
        text=f"{date.month}/{date.day} ",
        font=get_font(20),
        point=date_area.center_point,
        canvas=canvas,
        align=TextAlign.Center,
        y_delta=10,
    ).draw()


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

weather_col = weather_row.add_col()
weather_col.gutter = 10
row1 = weather_col.add_row()
row1.set_height(200)
detail_row = weather_col.add_row()
detail_row.set_height(140)

row1.gutter = 10
today = row1.add_col()
day2 = row1.add_col()
day3 = row1.add_col()
day4 = row1.add_col()
day5 = row1.add_col()

fill_today_content(today, canvas=canvas)
fill_next_days_content(
    day2, canvas=canvas, date=datetime.datetime.now() + datetime.timedelta(days=1)
)
fill_next_days_content(
    day3, canvas=canvas, date=datetime.datetime.now() + datetime.timedelta(days=2)
)
fill_next_days_content(
    day4, canvas=canvas, date=datetime.datetime.now() + datetime.timedelta(days=3)
)
fill_next_days_content(
    day5, canvas=canvas, date=datetime.datetime.now() + datetime.timedelta(days=4)
)

detail_cols = []
for x in range(5):
    detail_cols.append(detail_row.add_col())

for x in range(len(detail_cols)):
    fill_detail_area(
        col=detail_cols[x],
        canvas=canvas,
        date=datetime.datetime.now() + datetime.timedelta(days=x),
    )

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
