import dacite
import datetime

from libs.canvas import Canvas
from libs.layout import Column, Row
from libs.shapes import Point
from libs.text import Text, TextAlign
from libs.icon import IconSun,IconCloud,IconRain,IconSnow
from libs.line import Line
from libs.font import get_font
from apps.weather.model.weather import Weather
from apps.weather.service.read_data import get_update_time, get_weather_by_date


def fill_today_content(col: Column, canvas: Canvas):
    icon_area = col.add_row()
    temperature_area = col.add_row()
    temperature_area_number = temperature_area.add_col()
    _ = temperature_area.add_col()
    degree_area = _.add_row()
    text_area = _.add_row()
    data = get_weather_by_date(date=datetime.datetime.now())
    weather = dacite.from_dict(data_class=Weather, data=data)
    IconSun(center_point=icon_area.center_point, canvas=canvas, size=30, width=5, lines_count=7).draw()
    Text(text=f"{weather.tempMax}", font=get_font(70), point=Point(temperature_area_number.x, temperature_area_number.center_point.y), canvas=canvas, align=TextAlign.Left).draw()
    Text(text="°C", font=get_font(24), point=degree_area.center_point, canvas=canvas, y_delta=5).draw()
    Text(text=f"{weather.textDay}", font=get_font(24), point=text_area.center_point, canvas=canvas, align=TextAlign.Left, y_delta=-15).draw()
    




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
calendar_col1 = calendar_row.add_col()
calendar_col5 = calendar_row.add_col()
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
    font=get_font(),
    point=Point(x=calendar_col1.x, y=calendar_col1.center_point.y),
    canvas=canvas,
    align=TextAlign.Right,
).draw()
update_time = Text(
    text=f"Update Time: {get_update_time()}",
    font=get_font(20),
    point=Point(x=calendar_col5.x, y=calendar_col5.center_point.y),
    canvas=canvas,
    align=TextAlign.Right,
    x_delta=-40
).draw()



col = Column(
    canvas=canvas,
    x=BASIC_X,
    y=calendar_row.end_y + 60,
    width=canvas.width - BASIC_X * 2,
    height=canvas.height - 2 * BORDER_WIDTH - STARTING_Y - calendar_row.end_y,
)
col.gutter = 10
row1 = col.add_row()
row1.set_height(200)

row1.gutter = 10
today = row1.add_col()
day2 = row1.add_col()
day3 = row1.add_col()
day4 = row1.add_col()
day5 = row1.add_col()

fill_today_content(today, canvas=canvas)

IconSun(center_point=day4.center_point, canvas=canvas, size=30, width=5, lines_count=7).draw()
IconCloud(center_point=day3.center_point, canvas=canvas, size=30, width=5).draw()
IconRain(center_point=day2.center_point, canvas=canvas, size=30, width=5).draw()
# IconSnow(center_point=day1.center_point, canvas=canvas, size=30, width=5).draw()


canvas.save("weather.bmp")
