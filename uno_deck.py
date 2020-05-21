from random import randint
from card import Card
from constants import *

class UnoDeck:
    NUMBER_OF_DUP_REGULAR_CARDS = 2
    NUMBER_OF_DUP_ZERO_CARDS = 1
    NUMBER_OF_DUP_SPECIAL_CARDS = 2
    NUMBER_OF_WILD_CARDS = 4
    NUMBER_OF_WILD_D4_CARDS = 4
    SHUFFLE_FACTOR = 1

    def __init__(self):
        self.cards = []
        self.discarded_cards = []
        self.fill_deck()

    def fill_deck(self):
      for i in range(self.NUMBER_OF_DUP_REGULAR_CARDS):
        for num in range(9):
          self.cards.append(Card.number_card(Color.RED, num+1))
          # TODO: add remaining colors
      
      # TODO: add rest of cards (should be 108 total)
      # use the constants defined above ("NUMBER_OF...")
      # do some research to find out what cards are needed
      # for examples of how to create other types of cards,
      # scroll the test_card_print function of the uno_test.py file
        

    def shuffle(self):
      # TODO: write this function:
      # for some number of times
      # (how many? you pick a good number.
      # then multiply that number by SHUFFLE_FACTOR (defined above)
      # so people can "double" or "triple" the number of times you picked)
        # pick two items randomly from the list called self.cards
        # and swap their positions in the list
      # don't return anything.
      pass

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
