from dataclasses import dataclass


@dataclass
class Rectangle:
    x: int  # starting X coordinate
    y: int  # starting Y coordinate
    width: int
    height: int

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


@dataclass
class Point:
    x: int  # starting X coordinate
    y: int  # starting Y coordinate

    def __init__(self, x, y):
        self.x = x
        self.y = y
