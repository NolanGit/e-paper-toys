from dataclasses import dataclass


@dataclass
class Aqi:
    fxDate: str
    aqi: str
    level: str
    category: str
    primary: str
