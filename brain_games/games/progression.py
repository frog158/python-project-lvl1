# -*- coding:utf-8 -*-

"""Progression game."""


from random import randint

ASK_STR = 'What number is missing in the progression?'


def generate_progression():
    """Генерирует начало дельту и ответ.

    Returns:
        Возворащает кортеж
    """
    START_OF_PROGRESSION = 1
    END_OF_PROGRESSION = 20
    start_of_progression = randint(START_OF_PROGRESSION, END_OF_PROGRESSION)
    START_OF_DELTA = 1
    END_OF_DELTA = 10
    delta = randint(START_OF_DELTA, END_OF_DELTA)
    START_OF_ANSWER = 1
    END_OF_ANSWER = 10
    answer = randint(START_OF_ANSWER, END_OF_ANSWER)

    return (start_of_progression, delta, answer)


def generate_question_and_answer():
    """Generate question and answer.

    Returns:
            retruns - tuple of question and answer
    """
    LEN_OF_PROGRESSION = 10
    progression = generate_progression()
    index = 1
    question = ''
    answer = 0
    progression_start = progression[0]
    while index <= LEN_OF_PROGRESSION:
        if index == progression[2]:
            question = '{0}{1} '.format(question, '..')
            answer = progression_start
        else:
            question = '{0}{1} '.format(question, str(progression_start))
        progression_start += progression[1]
        index += 1
    return (question, str(answer))
