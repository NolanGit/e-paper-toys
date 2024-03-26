import datetime

from libs.shapes import Point
from libs.canvas import Canvas
from libs.font import get_font
from libs.csv_icon import CsvIcon
from apps.weather.model.icon import EIcon
from libs.layout import Column, Row
from libs.text import Text, TextAlign
from libs.icon import IconSun, IconCloud, IconRain, IconSnow

from apps.weather.service.data import (
    get_update_time,
    get_weather_by_date,
    get_aqi_by_date,
)

WEEK_DICT = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}


def draw_sun_icon(canvas: Canvas, center_point: Point):
    CsvIcon(
        icon=EIcon.day_sunny, canvas=canvas, center_point=center_point, size=120
    ).draw()


def draw_cloud_icon(canvas: Canvas, center_point: Point):
    CsvIcon(icon=EIcon.cloud, canvas=canvas, center_point=center_point, size=100).draw()


def draw_rain_icon(canvas: Canvas, center_point: Point):
    CsvIcon(icon=EIcon.snow, canvas=canvas, center_point=center_point, size=100).draw()


def draw_snow_icon(canvas: Canvas, center_point: Point):
    CsvIcon(icon=EIcon.snow, canvas=canvas, center_point=center_point, size=100).draw()


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
    detail_area = col.add_row()
    temperature_area_number = temperature_area.add_col()
    _ = temperature_area.add_col()
    degree_area = _.add_row()
    text_area = _.add_row()
    weather = get_weather_by_date(date=datetime.datetime.now())
    if int(weather.iconDay) == 100:
        draw_sun_icon(canvas=canvas, center_point=icon_area.center_point)
    elif int(weather.iconDay) < 200:
        draw_cloud_icon(canvas=canvas, center_point=icon_area.center_point)
    elif int(weather.iconDay) < 400:
        draw_rain_icon(canvas=canvas, center_point=icon_area.center_point)
    elif int(weather.iconDay) < 500:
        draw_snow_icon(canvas=canvas, center_point=icon_area.center_point)
    Text(
        text=f"{weather.tempMax}",
        font=get_font(60),
        point=Point(
            temperature_area_number.end_x, temperature_area_number.center_point.y
        ),
        canvas=canvas,
        align=TextAlign.Left,
    ).draw()

    CsvIcon(
        icon=EIcon.celsius,
        canvas=canvas,
        center_point=Point(degree_area.center_point.x, degree_area.center_point.y + 15),
        size=80,
    ).draw()

    Text(
        text=f"{weather.textDay}",
        font=get_font(24),
        point=Point(text_area.x, text_area.center_point.y),
        canvas=canvas,
        align=TextAlign.Right,
        y_delta=-15,
        x_delta=5,
    ).draw()
    detail_col = detail_area.add_col()
    fill_detail_area(col=detail_col, canvas=canvas, date=datetime.datetime.now())


def fill_next_days_content(col: Column, canvas: Canvas, date: datetime.datetime):
    week_area = col.add_row()
    week_area.set_height(45)
    date_area = col.add_row()
    date_area.set_height(38)
    icon_area = col.add_row()
    icon_area.set_height(130)
    detail_area = col.add_row()
    weather = get_weather_by_date(date=date)
    if int(weather.iconDay) == 100:
        draw_sun_icon(canvas=canvas, center_point=icon_area.center_point)
    elif int(weather.iconDay) < 200:
        draw_cloud_icon(canvas=canvas, center_point=icon_area.center_point)
    elif int(weather.iconDay) < 400:
        draw_rain_icon(canvas=canvas, center_point=icon_area.center_point)
    elif int(weather.iconDay) < 500:
        draw_snow_icon(canvas=canvas, center_point=icon_area.center_point)
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
    detail_col = detail_area.add_col()
    fill_detail_area(col=detail_col, canvas=canvas, date=date)


canvas = Canvas(800, 480)

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


_text = f"{WEEK_DICT[datetime.datetime.now().weekday()]} {datetime.datetime.now().month}/{datetime.datetime.now().day}"
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


col = Column(
    canvas=canvas,
    x=BASIC_X,
    y=calendar_row.end_y + 10,
    width=canvas.width - BASIC_X * 2,
    height=canvas.height - STARTING_Y - calendar_row.end_y,
)
col.gutter = 10
row1 = col.add_row()
row1.set_height(320)

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
# IconSun(
#     center_point=day4.center_point, canvas=canvas, size=30, width=5, lines_count=7
# ).draw()
# IconCloud(center_point=day3.center_point, canvas=canvas, size=30, width=5).draw()
# IconRain(center_point=day2.center_point, canvas=canvas, size=30, width=5).draw()
# IconSnow(center_point=day1.center_point, canvas=canvas, size=30, width=5).draw()


canvas.save("weather.bmp")
# canvas.draw_in_epd()
