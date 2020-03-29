import itertools
import random

class Casino:
    def __init__(self, name: str):
        self.name = name
        self.card = 0
        self.count = 0

    def __repr__(self):
        return f'{self.name}'


class Card:
    pass

    def deck():
        value_c = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        type_c = ["\u2663", "\u2663", "\u2665", "\u2660"]
        decks = list(itertools.product(value_c, type_c))
        random.shuffle(decks)
        print(decks)
        return


# value_c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, 12, 13]
# type_c = ["\u2663", "\u2663", "\u2665", "\u2660"]
# decks = list(itertools.product(value_c, type_c))
# random.shuffle(decks)


