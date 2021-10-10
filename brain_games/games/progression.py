# -*- coding:utf-8 -*-

"""Progression game."""


from random import randint


def generate_start_progression():
    """Generate start of progression.

    Returns:
        start of progression
    """
    START_OF_RANGE = 1
    END_OF_RANGE = 20
    return randint(START_OF_RANGE, END_OF_RANGE)


def generate_delta():
    """Generate delta.

    Returns:
        delta of progression
    """
    START_OF_RANGE = 1
    END_OF_RANGE = 9
    return randint(START_OF_RANGE, END_OF_RANGE)


def generate_answer():
    """Generate answer.

    Returns:
        return answer
    """
    START_OF_RANGE = 1
    END_OF_RANGE = 10
    return randint(START_OF_RANGE, END_OF_RANGE)


def generate_progression():
    """Генерирует начало дельту и ответ.

    Returns:
        Возворащает кортеж
    """
    return (generate_start_progression(), generate_delta(), generate_answer())


def generate_question():
    """Generate question and answer.

    Returns:
            retruns - tuple of question and answer
    """
    progression = generate_progression()
    index = 1
    question = ''
    answer = 0
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


def get_start_msg():
    """Return start message.

    Returns:
        returns - string. Start message
    """
    return 'What number is missing in the progression?'
