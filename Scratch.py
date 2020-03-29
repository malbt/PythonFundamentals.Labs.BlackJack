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

class Draw:
    pass

    def player(n):
        for i in range(n):
            print("player: ", Card.deck[i][0], Card.deck[i][1])

    def dealer(n):
        for i in range(n):
            print("dealer: ", Card.deck[i][0], Card.deck[i][1])



class Point:

    # def __init__(self):
    #     self.count = []
    #     self.card = []

    def add_person(self, Casino.person) -> None:
        self.person = Casino(self.person)

    def cardPoint(player_cards):
        player_count = 0
        ace_count = 0

        for i in player_cards:
            if i[1] == "J" or i[1] == "Q" or i[1] == "K":
                player_count += 10
            elif i[1] != "A":
                player_count += int(i[1])
            else:
                ace_count += 1
        if ace_count == 1 and player_count >= 10:
            player_count += 11
        else:
            player_count += 1

        return player_count


class Game:
    pass

    def start_game:
        player_cards = [Card.deck.pop(), Card.deck.pop()]
        dealer_cards = [Card.deck.pop(), Card.deck.pop()]

    def option():
        option = input("choice-> HIT ,  FOLD")
        return option.upper()

    def game_cont():
        if Game.option == "Hit":
            player_cards.append(Card.deck.pop())
        elif Point.cardPoint(player_cards) < Point.cardPoint(dealer_cards)
        elif Game.option == "FOLD":

    # player_cards = [Card.deck.pop(), Card.deck.pop()]
    # dealer_cards = [Card.deck.pop(), Card.deck.pop()]
    # while cardPoint(dealer_cards) <= 15:
    #     dealer_cards.append(Card.deck.pop())
