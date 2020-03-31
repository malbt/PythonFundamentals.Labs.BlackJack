import unittest
from typing import Callable
from unittest.mock import patch

from nose.plugins.builtin import builtins

from black_jack import option
import black_jack
import random


class TestBlackJack(unittest.TestCase):

    def test_result(self):
        if sum(black_jack.dealer_card) < sum(black_jack.player_card) <= 21:
            black_jack.result = {"player wins"}
        if sum(black_jack.dealer_card) == sum(black_jack.player_card) <= 21:
            black_jack.result = {"it's a tie"}
        if sum(black_jack.dealer_card) > sum(black_jack.player_card) <= 21:
            black_jack.result = {"dealer wins"}
        if sum(black_jack.player_card) > 21 and sum(black_jack.dealer_card) <= 21:
            black_jack.result = {"dealer wins"}

    #
    # val = "hit"
    #
    # @patch('builtins.input', return_value=val)
    # def test_option(self, mock_input):
    #     self.assertEqual("HIT", black_jack.option())
    #
    # #val = "hit"

    # @patch('builtins.input', return_value=val)
    # def test_option(self, mock_input):
    #     result = black_jack.option()
    #     self.assertEqual("HIT", result)
    # val1 = []

    # while len(dealer_card) != 2:
    #     dealer_card.append(random.randint(1, 11))
    #
    # @patch('random.randint')
    # @patch(black_jack.dealer_card.append.mock_randint)
    # def test_dealers_card(self):
    #     while black_jack.dealer_card != 2:
    #         val = []
    #         result = val
    #         self.assertEqual(result, val)
    #         if len(black_jack.dealer_card) == 2:
    #             black_jack.dealers_card = {"dealer_card:hidden card &", black_jack.dealer_card[1]}
    #         elif len(black_jack.dealer_card) == 2 and black_jack.option() != "HIT":
    #             black_jack.dealers_card = {"dealer_card:", black_jack.dealer_card, sum(black_jack.dealer_card)}
    #         elif len(black_jack.dealer_card) == 2 and black_jack.option() == "HIT":
    #             black_jack.dealers_card = {"dealer_card:", black_jack.dealer_card, sum(black_jack.dealer_card)}

    # def option():
    #     choice = input("choice-> HIT ,  STAY:").upper()
    #     # choice = choice.upper()
    #     print(choice)
    #     return
    val = "hit"

    @patch('builtins.input', return_value=val)
    def test_option():
        result = black_jack.option()
        builtins.input.assertEqual(result, "HIT")
