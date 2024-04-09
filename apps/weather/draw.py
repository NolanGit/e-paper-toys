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
from apps.const import WEEK_DICT


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
        align=TextAlign.Left,
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
        y_delta=0.033*col.height,
    ).draw()

    Text(
        text=f"{weather.textDay}",
        font=get_font(24),
        point=Point(text_area.center_point.x, text_area.center_point.y),
        canvas=canvas,
        align=TextAlign.Center,
        y_delta=-0.05*col.height,
        x_delta=0.037*col.width,
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
        y_delta=0.033*col.height,
    ).draw()


def draw(canvas: Canvas, row: Row):
    weather_col = row.add_col()
    weather_col.gutter = row.width * 0.012
    row1 = weather_col.add_row()
    row1.set_height(row.height * 0.6)
    detail_row = weather_col.add_row()
    detail_row.set_height(row.height * 0.4)

    row1.gutter = row.width * 0.03
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
