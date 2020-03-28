import itertools
import random


class Card:
    pass

    def deck():
        value_c = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        type_c = ["\u2663", "\u2663", "\u2665", "\u2660"]
        decks = list(itertools.product(value_c, type_c))
        random.shuffle(decks)
        print(decks)
        return


# value_c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# type_c = ["\u2663", "\u2663", "\u2665", "\u2660"]
# decks = list(itertools.product(value_c, type_c))
# random.shuffle(decks)


class Draw:
    pass

    def player(n):
        for i in range(n):
            print("player: ", Card.deck[i][0], Card.deck[i][1])

    def dealer(n):
        for i in range(n):
            print("dealer: ", Card.deck[i][0], Card.deck[i][1])


class Game:
    pass

    while sum(player) < 21:
        option = input("choice-> Hit  or  fold")
        if option == 'fold':
            break
        elif option == 'Hit':
            Draw.player(n)
        else:
            print("invalid entry")
