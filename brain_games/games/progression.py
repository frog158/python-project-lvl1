# -*- coding:utf-8 -*-

"""Progression game."""


from random import randint

from brain_games.games.games_engine import start_engine


def generate_progression():
    """Генерирует начало дельту и ответ.

    Returns:
        Возворащает кортеж
    """
    start_progression = 20
    return (randint(1, start_progression), randint(1, 9), randint(1, 9))


def gerate_tuple_of_question():
    """Generate question and answer.

    Returns:
            retruns - tuple of question and answer
    """
    progression = generate_progression()
    index = 1
    question = ''
    progression_start = progression[0]

    while index <= 10:
        if index == progression[2]:
            question = '{0}{1} '.format(question, '..')
            answer = progression_start
        else:
            question = '{0}{1} '.format(question, str(progression_start))
        progression_start += progression[1]
        index += 1
    return (question, str(answer))


def start_game():
    """Start of progression game.

    We will ask user three question.
    """
    index = 1
    list_of_question = []
    while index <= 3:
        list_of_question.append(gerate_tuple_of_question())
        index += 1
    ask_string = 'What number is missing in the progression?'
    start_engine(ask_string, list_of_question)
