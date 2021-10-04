# -*- coding:utf-8 -*-

"""Gdc game."""


from random import randint

from brain_games.games.games_engine import start_engine


def find_gcd(x1, x2):
    """Find the gdc of.

    Args:
        x1: one
        x2: two

    Returns:
        returns: gcd of tow integer
    """
    while x1 != 0 and x2 != 0:
        if x1 > x2:
            x1 %= x2
        else:
            x2 %= x1
    return (x1 + x2)


def gerate_tuple_of_question():
    """Generate question and answer.

    Returns:
            retruns - tuple of question and answer
    """
    x1 = randint(1, 100)
    x2 = randint(1, 100)
    answer = find_gcd(x1, x2)
    return ('{0} {1}'.format(str(x1), str(x2)), str(answer))


def start_game():
    """Start of calc game.

    We will ask user three question.
    """
    index = 1
    list_of_question = []
    while index <= 3:
        list_of_question.append(gerate_tuple_of_question())
        index += 1
    ask_string = 'Find the greatest common divisor of given numbers.'
    start_engine(ask_string, list_of_question)
