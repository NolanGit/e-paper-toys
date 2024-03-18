import os
import json
import datetime


def read_data():
    with open(f"{os.getcwd()}/apps/weather/data") as f:
        return f.read()


def get_update_time():
    data = read_data()
    update_time = json.loads(data)["updateTime"]
    return update_time.replace("T", " ").replace("+08:00", "")


def get_weather_by_date(date: datetime.datetime):
    date_str = date.strftime("%Y-%m-%d")
    for item in json.loads(read_data()).get("daily", []):
        if item.get("fxDate", "") == date_str:
            return item
    return {}


if __name__ == "__main__":
    print(get_update_time())
    print(get_weather_by_date(datetime.datetime.now()))
