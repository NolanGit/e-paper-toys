from dataclasses import dataclass


@dataclass
class Aqi:
    fxDate: str = None
    aqi: str = None
    level: str = None
    category: str = None
    primary: str = None
