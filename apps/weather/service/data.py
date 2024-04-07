import os
import json
import dacite
import datetime

from apps.weather.model.weather import Weather
from apps.weather.model.aqi import Aqi


def read_data(file_name: str = "15d_data"):
    with open(f"{os.getcwd()}/apps/weather/resource/{file_name}") as f:
        return f.read()


def write_data(text: str, file_name: str = "15d_data"):
    with open(f"{os.getcwd()}/apps/weather/resource/{file_name}", "w") as f:
        return f.write(text)


def get_update_time() -> str:
    data = read_data()
    update_time = json.loads(data)["updateTime"]
    _ = update_time.replace("T", " ").replace("+08:00", "")
    return '-'.join(_.split("-")[1:])


def get_weather_by_date(date: datetime.datetime) -> Weather:
    date_str = date.strftime("%Y-%m-%d")
    for item in json.loads(read_data("15d_data")).get("daily", []):
        if item.get("fxDate", "") == date_str:
            return dacite.from_dict(data_class=Weather, data=item)
    return Weather()


def get_aqi_by_date(date: datetime.datetime) -> dict:
    date_str = date.strftime("%Y-%m-%d")
    for item in json.loads(read_data("aqi_data")).get("daily", []):
        if item.get("fxDate", "") == date_str:
            return dacite.from_dict(data_class=Aqi, data=item)
    return Aqi()


if __name__ == "__main__":
    print(get_update_time())
    print(get_weather_by_date(datetime.datetime.now()))
