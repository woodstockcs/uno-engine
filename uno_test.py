from card import Card
from constants import *
from deck import Deck


def test_card_print():

    print()
    print("-------------------")
    print("default constructor")
    print("-------------------")

    print("wild: ", end='')
    c = Card(Color.NONE, Rank.WILD, 0)
    print(c)

    print("green 3: ", end='')
    c = Card(Color.GREEN, Rank.NUMBER, 3)
    print(c)

    print("red 7: ", end='')
    c = Card(Color.RED, Rank.NUMBER, 7)
    print(c)

    print("blue draw-two: ", end='')
    c = Card(Color.BLUE, Rank.DRAW_TWO, 0)
    print(c)

    print("red draw-two: ", end='')
    c = Card(Color.RED, Rank.DRAW_TWO, 0)
    print(c)

    print("wild draw-four: ", end='')
    c = Card(Color.NONE, Rank.WILD_D4, 0)
    print(c)

    print()
    print("--------------------------")
    print("nonnumber_card constructor")
    print("--------------------------")

    print("wild: ", end='')
    c = Card.nonnumber_card(Color.NONE, Rank.WILD)
    print(c)

    print("yellow reverse: ", end='')
    c = Card.nonnumber_card(Color.YELLOW, Rank.REVERSE)
    print(c)

    print("green skip: ", end='')
    c = Card.nonnumber_card(Color.GREEN, Rank.SKIP)
    print(c)

    print()
    print("-----------------------")
    print("number_card constructor")
    print("-----------------------")

    print("red 4: ", end='')
    c = Card.number_card(Color.RED, 4)
    print(c)

    print("yellow 1: ", end='')
    c = Card.number_card(Color.YELLOW, 1)
    print(c)



def test_card_forfeit_cost():

    print()
    print("-----------------------")
    print("forfeit_cost")
    print("-----------------------")

    print("BS should be 20: ", end='')
    c = Card(Color.BLUE, Rank.SKIP, 0)
    print(c.forfeit_cost())

    print("RR should be 20: ", end='')
    c = Card(Color.RED, Rank.REVERSE, 0)
    print(c.forfeit_cost())

    print("Y+2 should be 20: ", end='')
    c = Card(Color.YELLOW, Rank.DRAW_TWO, 0)
    print(c.forfeit_cost())

    print("W should be 50: ", end='')
    c = Card(Color.NONE, Rank.WILD, 0)
    print(c.forfeit_cost())

    print("W+4 should be 50: ", end='')
    c = Card(Color.NONE, Rank.WILD_D4, 0)
    print(c.forfeit_cost())

    print("B4 should be 4: ", end='')
    c = Card(Color.BLUE, Rank.NUMBER, 4)
    print(c.forfeit_cost())

    print("R0 should be 0: ", end='')
    c = Card(Color.RED, Rank.NUMBER, 0)
    print(c.forfeit_cost())


def test_deck():

    print()
    print("-----------------------")
    print("deck")
    print("-----------------------")

    print("deck size should be 108: ", end='')
    d = Deck()
    print(len(d.cards))
    
    print()
    print("all the cards:")
    print(', '.join([str(c) for c in d.cards]))

    print()
    print("first ten cards before a shuffle:")
    d = Deck()
    for i in range(9):
      print(d.cards[i], end=", ")
    print(d.cards[9])

    print()
    print("first ten cards after a shuffle:")
    d.shuffle()
    for i in range(9):
      print(d.cards[i], end=", ")
    print(d.cards[9])   

    print()
    print("is_empty should be False: ", end='')
    print(d.is_empty())

    print()
    print("draw all cards: ", end='')
    while len(d.cards) > 0:
      d.draw()
    print("done")
    print("is_empty should be True: ", end='')
    print(d.is_empty())

def main():
    print("\n")
    print("*******************************")
    print("*                             *")
    print("*    UNO ENGINE TEST SUITE    *")
    print("*                             *")
    print("*******************************")
    test_card_print()
    # test_card_forfeit_cost()
    test_deck()

if __name__ == '__main__':
    main()
