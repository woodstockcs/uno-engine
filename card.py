from constants import *
from termcolor import cprint

class Card:
    """ implements the functionatily of a Card """

    def __init__(self, color, rank, number):
        self.color = color
        self.rank = rank
        self.number = number

    @classmethod
    def number_card(cls, color, number):
        return cls(color, Rank.NUMBER, number)

    @classmethod
    def nonnumber_card(cls, color, rank):
        return cls(color, rank, -1)

    def __str__(self):
        output = ""
        PRINT_IN_COLOR = False
        if PRINT_IN_COLOR:
            if self.color == Color.RED:
                output += "\033[31m"
            # TODO: add remaining colors using elif

        if self.color == Color.RED:
          output += "R"
        elif self.color == Color.YELLOW:
          output += "Y"
        elif self.color == Color.GREEN:
          output += "G"
        elif self.color == Color.BLUE:
          output += "B"

        if self.rank == Rank.WILD:
          output += "W"
        elif self.rank == Rank.SKIP:
          output += "S"
        elif self.rank == Rank.REVERSE:
          output += "R"
        elif self.rank == Rank.DRAW_TWO:
          output += "+2"
        elif self.rank == Rank.WILD_D4:
          output += "W+4"
        elif self.rank == Rank.NUMBER:
          output += str(self.number)

        if PRINT_IN_COLOR:
            output += "\033[37m\033[0m"
        return output

    def forfeit_cost(self):
      
      if self.rank == Rank.SKIP:
        return 20
      elif self.rank == Rank.REVERSE:
        return 20
      elif self.rank == Rank.DRAW_TWO:
        return 20
      if self.rank == Rank.WILD or Rank.WILD_DRAW_FOUR:
        return 50
      
      return self.number + int(self.color)
        

    def can_play_on(self, c, calledColor):
        if self.rank == Rank.WILD:
            return True
        if self.rank == Rank.WILD_D4:
            return True

    def perform_card_effect(self, game):
        if self.rank == Rank.SKIP:
            game.advance_to_next_player()
        game.advance_to_next_player()
        
