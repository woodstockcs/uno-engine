from card import Card
from constants import *
from deck import Deck

def test(expected, actual):
    print(f"expected = {expected}")
    print(f"actual   = {actual}")
    if expected == actual:
        print("\033[32mTEST PASSED :-) \033[37m\033[0m")
    else:
        print("\033[31mTEST FAILED :-( \033[37m\033[0m")

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

def test_card_can_play_on():

    print()
    print("-----------------------")
    print("card.can_play_on")
    print("-----------------------")


    print()
    print("Can a WILD play on RED 3?")
    expected = True
    actual = Card(Color.NONE, Rank.WILD, 0).can_play_on(Card(Color.RED, Rank.NUMBER, 3), Color.NONE)
    test(expected, actual)

    print()
    print("Can a WILD play on WILD when BLUE is called?")
    expected = True
    actual = Card(Color.NONE, Rank.WILD, 0).can_play_on(Card(Color.NONE, Rank.WILD, 0), Color.BLUE)
    test(expected, actual)

    print()
    print("Can a WILD_D4 play on RED REVERSE?")
    expected = True
    actual = Card(Color.NONE, Rank.WILD_D4, 0).can_play_on(Card(Color.RED, Rank.REVERSE, 0), Color.NONE)
    test(expected, actual)

    print()
    print("Can a BLUE 3 play on BLUE 5?")
    expected = True
    actual = Card(Color.BLUE, Rank.NUMBER, 3).can_play_on(Card(Color.BLUE, Rank.NUMBER, 5), Color.NONE)
    test(expected, actual)

    print()
    print("Can a BLUE 3 play on RED 5?")
    expected = False
    actual = Card(Color.BLUE, Rank.NUMBER, 3).can_play_on(Card(Color.RED, Rank.NUMBER, 5), Color.NONE)
    test(expected, actual)

    print()
    print("Can a BLUE 3 play on WILD when BLUE is called?")
    expected = True
    actual = Card(Color.BLUE, Rank.NUMBER, 3).can_play_on(Card(Color.NONE, Rank.WILD, 0), Color.BLUE)
    test(expected, actual)

    print()
    print("Can a BLUE 3 play on WILD when YELLOW is called?")
    expected = False
    actual = Card(Color.BLUE, Rank.NUMBER, 3).can_play_on(Card(Color.NONE, Rank.WILD, 0), Color.YELLOW)
    test(expected, actual)

    print()
    print("Can a BLUE REVERSE play on RED REVERSE?")
    expected = True
    actual = Card(Color.BLUE, Rank.REVERSE, 0).can_play_on(Card(Color.RED, Rank.REVERSE, 0), Color.NONE)
    test(expected, actual)

    print()
    print("Can a BLUE REVERSE play on GREEN SKIP?")
    expected = False
    actual = Card(Color.BLUE, Rank.REVERSE, 0).can_play_on(Card(Color.GREEN, Rank.SKIP, 0), Color.NONE)
    test(expected, actual)

    print()
    print("Can a GREEN 4 play on RED 4?")
    expected = True
    actual = Card(Color.GREEN, Rank.NUMBER, 4).can_play_on(Card(Color.RED, Rank.NUMBER, 4), Color.NONE)
    test(expected, actual)

    print()
    print("Can a GREEN 4 play on RED 5?")
    expected = False
    actual = Card(Color.GREEN, Rank.NUMBER, 4).can_play_on(Card(Color.RED, Rank.NUMBER, 5), Color.NONE)
    test(expected, actual)


def test_deck():

    print()
    print("-----------------------")
    print("deck")
    print("-----------------------")

    print()
    print("NUMBER_OF_REG_CARDS_PER_COLOR")
    expected = 2
    actual = Deck.NUMBER_OF_REG_CARDS_PER_COLOR
    test(expected, actual)

    print()
    print("NUMBER_OF_ZERO_CARDS_PER_COLOR")
    expected = 1
    actual = Deck.NUMBER_OF_ZERO_CARDS_PER_COLOR
    test(expected, actual)

    print()
    print("NUMBER_OF_SKIP_CARDS_PER_COLOR")
    expected = 2
    actual = Deck.NUMBER_OF_SKIP_CARDS_PER_COLOR
    test(expected, actual)

    print()
    print("NUMBER_OF_REVERSE_CARDS_PER_COLOR")
    expected = 2
    actual = Deck.NUMBER_OF_REVERSE_CARDS_PER_COLOR
    test(expected, actual)

    print()
    print("NUMBER_OF_DRAW_TWO_CARDS_PER_COLOR")
    expected = 2
    actual = Deck.NUMBER_OF_DRAW_TWO_CARDS_PER_COLOR
    test(expected, actual)

    print()
    print("NUMBER_OF_WILD_CARDS")
    expected = 4
    actual = Deck.NUMBER_OF_WILD_CARDS
    test(expected, actual)

    print()
    print("NUMBER_OF_WILD_D4_CARDS")
    expected = 4
    actual = Deck.NUMBER_OF_WILD_D4_CARDS
    test(expected, actual)

    print()
    print("deck size should be 108: ", end='')
    d = Deck()
    print(len(d.cards))

    print()
    print("all the cards:")
    if len(d.cards) > 0:
        print(', '.join([str(c) for c in d.cards]))
    else:
        print("no cards in deck")

    print()
    print("first ten cards before a shuffle:")
    d = Deck()
    if len(d.cards) > 0:
        for i in range(9):
          print(d.cards[i], end=", ")
        print(d.cards[9])
    else:
        print("no cards in deck")

    print()
    print("first ten cards after a shuffle:")
    if len(d.cards) > 0:
        d.shuffle()
        for i in range(9):
          print(d.cards[i], end=", ")
        print(d.cards[9])
    else:
        print("no cards in deck")

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
    test_card_can_play_on()

if __name__ == '__main__':
    main()
