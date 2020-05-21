from enum import Enum

class Color(Enum):
    NONE = 0
    RED = 1
    YELLOW = 2
    GREEN = 3
    BLUE = 4

class Rank(Enum):
    NUMBER = 0
    SKIP = 1
    REVERSE = 2
    DRAW_TWO = 3
    WILD = 4
    WILD_D4 = 5
