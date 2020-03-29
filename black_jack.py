import random

dealer_card = []


def dealers_card():
    while len(dealer_card) != 2:
        dealer_card.append(random.randint(1, 11))
        if len(dealer_card) == 2:
            print("dealer_card:hidden card & ", dealer_card[1])

        elif len(dealer_card) == 2 and option() != "HIT":
            print("dealer_card:", dealer_card, sum(dealer_card))
            return
        elif len(dealer_card) == 2 and option() == "HIT":
            print("dealer_card:", dealer_card, sum(dealer_card))
            return


player_card = []


def players_card():
    while len(player_card) != 2 or len(player_card) > 2:
        player_card.append(random.randint(1, 11))
        if len(player_card) == 2:
            print("players card: ", player_card, sum(player_card))
            return

        elif len(player_card) == 2 and option() == "HIT":
            player_card.append(random.randint(1, 11))
            print("players card: ", player_card, sum(player_card))
            return


def game():
    if option() == "HIT":
        player_card.append(random.randint(1, 11))
        print("players card: ", player_card, sum(player_card))
        print("dealer_card:", dealer_card, sum(dealer_card))
        return
    elif option != "HIT":
        player_card.append(random.randint(1, 11))
        print("players card: ", player_card, sum(player_card))
        print("dealer_card:", dealer_card, sum(dealer_card))
        return


def option():
    choice = input("choice-> HIT ,  STAY:")
    choice = choice.upper()
    print(choice)
    return choice


def result():
    if sum(dealer_card) < sum(player_card) <= 21:
        print("player wins")
        return
    elif sum(dealer_card) > sum(player_card) <= 21:
        print("dealer wins")
        return
    elif sum(dealer_card) == sum(player_card) <= 21:
        print("it's a tie")
        return
    elif sum(player_card) > 21 and sum(dealer_card) <= 21:
        print("dealer wins")
        return
    else:
        print("game over")
        return


if __name__ == '__main__':
    print("lets get started >>>")

players_card()
dealers_card()
game()
result()
