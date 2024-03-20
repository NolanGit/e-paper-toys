import os
import json
import datetime


def read_data(file_name: str = "weather_data"):
    with open(f"{os.getcwd()}/apps/weather/{file_name}") as f:
        return f.read()


def write_data(text: str, file_name: str = "weather_data"):
    with open(f"{os.getcwd()}/apps/weather/{file_name}", "w") as f:
        return f.write(text)


def get_update_time() -> str:
    data = read_data()
    update_time = json.loads(data)["updateTime"]
    return update_time.replace("T", " ").replace("+08:00", "")


def get_weather_by_date(date: datetime.datetime) -> dict:
    date_str = date.strftime("%Y-%m-%d")
    for item in json.loads(read_data()).get("daily", []):
        if item.get("fxDate", "") == date_str:
            return item
    return {}


def get_aqi_by_date(date: datetime.datetime) -> dict:
    date_str = date.strftime("%Y-%m-%d")
    for item in json.loads(read_data("aqi_data")).get("daily", []):
        if item.get("fxDate", "") == date_str:
            return item
    return {}


if __name__ == "__main__":
    print(get_update_time())
    print(get_weather_by_date(datetime.datetime.now()))
