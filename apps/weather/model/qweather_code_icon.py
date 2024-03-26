from apps.weather.model.icon import EIcon

ICON_DICT = {
    # day
    100: EIcon.day_sunny,  # 晴
    101: EIcon.cloudy,  # 多云
    102: EIcon.day_sunny_overcast,  # 少云
    103: EIcon.day_cloudy,  # 晴间多云
    300: EIcon.day_showers,  # 阵雨
    301: EIcon.day_rain,  # 强阵雨
    406: EIcon.day_rain_mix,  # 阵雨夹雪
    407: EIcon.day_snow,  # 阵雪
    # night
    150: EIcon.night_clear,  # 晴
    151: EIcon.night_alt_cloudy,  # 多云
    152: EIcon.night_alt_partly_cloudy,  # 少云
    153: EIcon.night_alt_cloudy,  # 晴间多云
    350: EIcon.night_alt_showers,  # 阵雨
    351: EIcon.night_alt_rain,  # 强阵雨
    456: EIcon.night_alt_rain_mix,  # 阵雨夹雪
    457: EIcon.night_alt_snow,  # 阵雪
    # all
    104: EIcon.cloud,  # 阴
    302: EIcon.thunderstorm,  # 雷阵雨
    303: EIcon.thunderstorm,  # 强雷阵雨
    304: EIcon.hail,  # 雷阵雨伴有冰雹
    305: EIcon.showers,  # 小雨
    306: EIcon.rain,  # 中雨
    307: EIcon.rain,  # 大雨
    308: EIcon.rain,  # 极端降雨
    309: EIcon.showers,  # 毛毛雨/细雨
    310: EIcon.rain,  # 暴雨
    311: EIcon.rain,  # 大暴雨
    312: EIcon.rain,  # 特大暴雨
    313: EIcon.hail,  # 冻雨
    314: EIcon.rain,  # 小到中雨
    315: EIcon.rain,  # 中到大雨
    316: EIcon.rain,  # 大到暴雨
    317: EIcon.rain,  # 暴雨到大暴雨
    318: EIcon.rain,  # 大暴雨到特大暴雨
    399: EIcon.rain,  # 雨
    400: EIcon.snow,  # 小雪
    401: EIcon.snow,  # 中雪
    402: EIcon.snow,  # 大雪
    403: EIcon.snow,  # 暴雪
    404: EIcon.rain_mix,  # 雨夹雪
    405: EIcon.rain_mix,  # 雨雪天气
    408: EIcon.snow,  # 小到中雪
    409: EIcon.snow,  # 中到大雪
    410: EIcon.snow,  # 大到暴雪
    499: EIcon.snow,  # 雪
    500: EIcon.haze,  # 薄雾
    501: EIcon.fog,  # 雾
    502: EIcon.dust,  # 霾
    503: EIcon.dust,  # 扬沙
    504: EIcon.dust,  # 浮尘
    507: EIcon.dust,  # 沙尘暴
    508: EIcon.dust,  # 强沙尘暴
    509: EIcon.fog,  # 浓雾
    510: EIcon.fog,  # 强浓雾
    511: EIcon.dust,  # 中度霾
    512: EIcon.dust,  # 重度霾
    513: EIcon.dust,  # 严重霾
    514: EIcon.fog,  # 大雾
    515: EIcon.fog,  # 特强浓雾
    900: EIcon.hot,  # 热
    901: EIcon.snowflake_code,  # 冷
    999: EIcon.na,  # 未知
}


class QweatherCode:
    code: int
    icon: EIcon

    def __init__(self, code: int):
        self.code = code
        return self

    @property
    def code(self):
        return ICON_DICT.get(self.code, EIcon.na)
