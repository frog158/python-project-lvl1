# -*- coding:utf-8 -*-

"""Calc game."""


from random import randint

from brain_games.games.games_engine import start_engine


def gerate_tuple_of_question():
    """Generate question and answer.

    Returns:
            retruns - tuple of question and answer
    """
    x1 = randint(1, 100)
    x2 = randint(1, 100)
    operator = randint(1, 3)
    if operator == 1:
        operator_string = '+'
        answer = str(x1 + x2)
    elif operator == 2:
        operator_string = '-'
        answer = str(x1 - x2)
    else:
        operator_string = '*'
        answer = str(x1 * x2)
    return ('{0} {2} {1}'.format(str(x1), str(x2), operator_string), answer)


def start_game():
    """Start of calc game.

    We will ask user three question.
    """
    index = 1
    list_of_question = []
    while index <= 3:
        list_of_question.append(gerate_tuple_of_question())
        index += 1
    start_engine(list_of_question)
