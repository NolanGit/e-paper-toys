import os
import sys
import requests

from apps.weather.service.data import write_data


"""
use qweather.com service
"""


def call_15d_weather_api(token: str, location_id: str, lang:str='en'):
    """
    location id: https://github.com/qwd/LocationList?tab=readme-ov-file
    """
    res = requests.get(f"https://devapi.qweather.com/v7/weather/15d?location={location_id}&key={token}&lang={lang}")
    write_data(text = res.text, file_name="15d_data")

def call_aqi_api(token: str, location_id: str, lang:str='en'):
    """
    location id: https://github.com/qwd/LocationList?tab=readme-ov-file
    """
    res = requests.get(f"https://devapi.qweather.com/v7/air/5d?location={location_id}&key={token}&lang={lang}")
    write_data(text = res.text, file_name="aqi_data")
    

if __name__ == "__main__":
    try:
        sys.argv[1]
        sys.argv[2]
    except IndexError as e:
        print("use qweather.com service, token and location id is required")
        exit()
    call_15d_weather_api(sys.argv[1], sys.argv[2])
    call_aqi_api(sys.argv[1], sys.argv[2])