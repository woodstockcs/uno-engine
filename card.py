from constants import *

class Card:
    """ implements the functionatily of a Card """

    def __init__(self, color, rank):
        self.color = color
        self.rank = rank
        self.number = -1

    def __init__(self, color, number):
        self.color = color
        self.rank = Rank.NUMBER
        self.number = number
