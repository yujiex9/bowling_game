from typing import List

import pytest

from bowling_game.game import Game


@pytest.fixture
def game():
    return Game()


def add_throws_of_pins_to_a_game(game: Game, throws: List[int]):
    # e.g. [1, 4, 4, 5], number of pins in each throw
    # in this game are 1, 4, 4, 5
    for pins in throws:
        game.add(pins)


def test_a_simple_first_throw_in_a_frame(game):
    add_throws_of_pins_to_a_game(game, [8])
    assert 8 == game.score
    assert 1 == game.current_frame


def test_two_simple_throws_in_a_frame(game):
    add_throws_of_pins_to_a_game(game, [2, 7])
    assert 9 == game.score
    assert 1 == game.current_frame


def test_simple_throws_in_two_frames(game):
    add_throws_of_pins_to_a_game(game, [1, 4, 4, 5])
    assert 5 == game.score_for_frame(1)
    assert 14 == game.score_for_frame(2)
    assert 14 == game.score
    assert 2 == game.current_frame


def test_a_simple_spare(game):
    add_throws_of_pins_to_a_game(game, [6, 4, 6, 3])
    assert 16 == game.score_for_frame(1)
    assert 25 == game.score_for_frame(2)
    assert 25 == game.score
    assert 2 == game.current_frame


def test_a_simple_strike(game):
    add_throws_of_pins_to_a_game(game, [10, 6, 3])
    assert 19 == game.score_for_frame(1)
    assert 28 == game.score_for_frame(2)
    assert 28 == game.score
    assert 2 == game.current_frame


def test_a_perfect_game(game):
    add_throws_of_pins_to_a_game(game, [10] * 12)
    assert 300 == game.score
    assert 10 == game.current_frame


def test_a_heart_broken_game(game):
    _throws = [10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 1, 1]
    add_throws_of_pins_to_a_game(game, _throws)
    assert 270 == game.score
    assert 10 == game.current_frame


def test_sample_game(game):
    _throws = [1, 4, 4, 5, 6, 4, 5, 5, 10, 0, 1, 7, 3, 6, 4, 10, 2, 8, 6]
    add_throws_of_pins_to_a_game(game, _throws)
    assert 133 == game.score
    assert 10 == game.current_frame
