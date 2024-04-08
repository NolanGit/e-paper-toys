import os
import datetime

from ics import Calendar

EN_DICT = {
    "元旦(休)": "New Year's Day (Holiday)",
    "元旦": "New Year's Day",
    "小寒": "Minor Cold",
    "大寒": "Major Cold",
    "春节(班)": "Spring Festival (Workday)",
    "春节(休)": "Spring Festival (Holiday)",
    "除夕": "New Year's Eve",
    "春节": "Spring Festival",
    "正月初二": "The Second Day of the First Month",
    "正月初三": "The Third Day of the First Month",
    "立春": "Start of Spring",
    "元宵节": "Lantern Festival",
    "雨水": "Rain Water",
    "惊蛰": "Waking of Insects",
    "妇女节": "International Women's Day",
    "春分": "Vernal Equinox",
    "清明(班)": "Clear and Bright (Workday)",
    "清明(休)": "Clear and Bright (Holiday)",
    "清明": "Clear and Bright",
    "谷雨": "Grain Rain",
    "劳动节(班)": "International Workers' Day (Workday)",
    "劳动节(休)": "International Workers' Day (Holiday)",
    "劳动节": "International Workers' Day",
    "青年节": "Youth Day",
    "立夏": "Start of Summer",
    "小满": "Grain Buds",
    "儿童节": "Children's Day",
    "端午节": "Dragon Boat Festival",
    "端午节(休)": "Dragon Boat Festival (Holiday)",
    "芒种": "Grain in Ear",
    "夏至": "Summer Solstice",
    "建党节": "The Founding of the Communist Party of China",
    "小暑": "Minor Heat",
    "大暑": "Major Heat",
    "建军节": "Army Day",
    "七夕节": "Qixi Festival",
    "立秋": "Start of Autumn",
    "处暑": "End of Heat",
    "白露": "Bai Lu",
    "中秋节(休)": "Mid-Autumn Festival (Holiday)",
    "中秋节": "Mid-Autumn Festival",
    "秋分": "Autumnal Equinox",
    "国庆节(休)": "National Day (Holiday)",
    "国庆节": "National Day",
    "重阳节": "Double Ninth Festival",
    "国庆节(班)": "National Day (Workday)",
    "寒露": "Cold Dew",
    "霜降": "Frost's Descent",
    "立冬": "Start of Winter",
    "小雪": "Minor Snow",
    "大雪": "Major Snow",
    "冬至": "Winter Solstice",
    "端午节(班)": "Dragon Boat Festival (Workday)",
    "中秋节(班)": "Mid-Autumn Festival (Workday)",
}


def get_current_event(date: datetime.datetime, file_name):
    with open(f"{os.getcwd()}/apps/calendar/resource/{file_name}") as f:
        _ = f.read()
    c = Calendar(_)
    events = sorted(c.events, key=lambda event: event.begin)

    result = []
    for e in events:
        if e.begin.datetime < date and e.end.datetime > date:
            e.name = EN_DICT[e.name]
            result.append(e)
    return result


def get_next_event(date: datetime.datetime, file_name):
    with open(f"{os.getcwd()}/apps/calendar/resource/{file_name}") as f:
        _ = f.read()
    c = Calendar(_)
    events = sorted(c.events, key=lambda event: event.begin)
    for e in events:
        if e.begin.datetime > date:
            e.name = EN_DICT[e.name]
            return e
    return None
