# -*- coding:utf-8 -*-

"""Progression game."""


from math import sqrt
from random import randint

from brain_games.games.games_engine import start_engine


def is_prime(num):
    """Проверяет простое число или нет .

    Args:
        num: число для проверки

    Returns:
        yes: если число простое
        no: если не простое
    """
    if num < 2:
        return 'no'
    if num == 2:
        return 'yes'
    limit = sqrt(num)
    index = 2
    while index <= limit:
        if num % index == 0:
            return 'no'
        index += 1
    return 'yes'


def gerate_tuple_of_question():
    """Generate question and answer.

    Returns:
            retruns - tuple of question and answer
    """
    num = randint(1, 100)
    answer = is_prime(num)
    return (str(num), answer)


def start_game():
    """Start of prime game.

    We will ask user three question.
    """
    index = 1
    list_of_question = []
    while index <= 3:
        list_of_question.append(gerate_tuple_of_question())
        index += 1
    ask_string = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    start_engine(ask_string, list_of_question)
