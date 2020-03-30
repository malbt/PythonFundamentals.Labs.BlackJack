import unittest
from typing import Callable
from unittest.mock import patch
from black_jack import option
import black_jack


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

    val = "hit"

    @patch('builtins.input', return_value=val)
    def test_option(self, mock_input):
        self.assertEqual("HIT", black_jack.option())

    #val = "hit"

    # @patch('builtins.input', return_value=val)
    # def test_option(self, mock_input):
    #     result = black_jack.option()
    #     self.assertEqual("HIT", result)


