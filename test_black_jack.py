import unittest
from typing import Callable
from unittest.mock import patch
from black_jack import option
import black_jack
import random
import random.randint(1, 11)


# noinspection PyShadowingNames
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
    val1 = []
    # while len(dealer_card) != 2:
    #     dealer_card.append(random.randint(1, 11))
    def test_dealers_card(self, append=None, val=None, val1=None):
        while val == val1:
            # result = val1(append.randint(1, 11))
            # self.assertEqual(result, append.randint(1, 11))
            if len(val1) == 2:
                black_jack.dealers_card = {"dealer_card:hidden card &", val1[1]}
            elif len(val1) == 2 and black_jack.option() != "HIT":
                black_jack.dealers_card = {"dealer_card:", val1, sum(val1)}
            elif len(val1) == 2 and black_jack.option() == "HIT":
                black_jack.dealers_card = {"dealer_card:", val1, sum(val1)}
