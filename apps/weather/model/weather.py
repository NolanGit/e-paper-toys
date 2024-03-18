from dataclasses import dataclass


@dataclass
class Weather:
    fxDate: str
    sunrise: str
    sunset: str
    moonrise: str
    moonset: str
    moonPhase: str
    moonPhaseIcon: str
    tempMax: str
    tempMin: str
    iconDay: str
    textDay: str
    iconNight: str
    textNight: str
    wind360Day: str
    windDirDay: str
    windScaleDay: str
    windSpeedDay: str
    wind360Night: str
    windDirNight: str
    windScaleNight: str
    windSpeedNight: str
    humidity: str
    precip: str
    pressure: str
    vis: str
    cloud: str
    uvIndex: str
