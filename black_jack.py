import random

dealer_card = []


def dealers_cards():
    while len(dealer_card) != 2:
        dealer_card.append(random.randint(1, 11))
        if len(dealer_card) == 2:
            # print("hidden card & ", dealer_card[1])
            print(dealer_card, sum(dealer_card))
            return


player_card = []


def players_card():
    while len(player_card) != 2:
        player_card.append(random.randint(1, 11))
        if len(player_card) == 2:
            print(player_card, sum(player_card))
            return


def option():
    choice = input("choice-> HIT ,  FOLD:")
    choice = choice.upper()
    print(choice)
    return choice


def game():
    if option() == "HIT":
        player_card.append(random.randint(1, 11))
        print("players card:", player_card)
        dealer_card.append(random.randint(1, 11))
        print("dealers_card:", dealer_card)
        result()
        return
    elif option != "HIT":
        result()
        return


def result():
    if sum(dealer_card) < sum(player_card) <= 21:
        print("player wins")
        return
    elif sum(player_card) < sum(dealer_card) <= 21:
        print("dealer wins")
        return
    elif sum(dealer_card) == sum(player_card) <= 21:
        print("it's a tie")
        return
    else:
        print("game over")
        return


if __name__ == '__main__':
    print("lets get started >>>")
players_card()
dealers_cards()
game()
