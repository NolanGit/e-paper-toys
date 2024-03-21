from dataclasses import dataclass


@dataclass
class Weather:
    fxDate: str = None
    sunrise: str = None
    sunset: str = None
    moonrise: str = None
    moonset: str = None
    moonPhase: str = None
    moonPhaseIcon: str = None
    tempMax: str = None
    tempMin: str = None
    iconDay: str = None
    textDay: str = None
    iconNight: str = None
    textNight: str = None
    wind360Day: str = None
    windDirDay: str = None
    windScaleDay: str = None
    windSpeedDay: str = None
    wind360Night: str = None
    windDirNight: str = None
    windScaleNight: str = None
    windSpeedNight: str = None
    humidity: str = None
    precip: str = None
    pressure: str = None
    vis: str = None
    cloud: str = None
    uvIndex: str = None
