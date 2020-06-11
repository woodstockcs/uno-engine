from random import randint
from card import Card
from constants import *

class Deck:
    NUMBER_OF_REG_CARDS_PER_COLOR = 2
    NUMBER_OF_ZERO_CARDS_PER_COLOR = 0
    NUMBER_OF_SKIP_CARDS_PER_COLOR = 2
    NUMBER_OF_REVERSE_CARDS_PER_COLOR = 0
    NUMBER_OF_DRAW_TWO_CARDS_PER_COLOR = 0
    NUMBER_OF_WILD_CARDS = 0
    NUMBER_OF_WILD_D4_CARDS = 0
    SHUFFLE_FACTOR = 0

    def __init__(self):
        self.cards = []
        self.discarded_cards = []
        self.fill_deck()

    def fill_deck(self):
      for i in range(self.NUMBER_OF_REG_CARDS_PER_COLOR):
        for num in range(9):
          self.cards.append(Card.number_card(Color.RED, num+1))
          # TODO: add remaining colors

      # TODO: add rest of cards (should be 108 total)
      # use the constants defined above ("NUMBER_OF...")
      # do some research to find out what cards are needed
      # for examples of how to create other types of cards,
      # scroll the test_card_print function of the uno_test.py file


    def shuffle(self):
      for i in range(len(self.cards) * self.SHUFFLE_FACTOR):
        pass
      # TODO:
        # pick two items randomly from the list called self.cards
        # and swap their positions in the list
      # don't return anything.

    def is_empty(self):
      if len(self.cards)==0:
        return True
      elif len(self.cards) > 0:
        return False
      pass

    def draw(self):
      if len(self.cards) > 0:
        return self.cards.pop(0)
      else:
        return None

    def discard(self, c):
        self.discarded_cards.append(c)

    def remix(self):
        self.cards.extend(self.discarded_cards)
        self.discarded_cards.clear()
        self.shuffle()
