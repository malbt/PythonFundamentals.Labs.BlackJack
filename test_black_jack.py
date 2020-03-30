import unittest
import black_jack


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


    def test_option(self):
