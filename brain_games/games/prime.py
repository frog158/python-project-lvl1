# -*- coding:utf-8 -*-

"""Progression game."""


from math import sqrt
from random import randint

ASK_STR = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    """Проверяет простое число или нет .

    Args:
        num: число для проверки

    Returns:
        yes: если число простое
        no: если не простое
    """
    if num < 2:
        return False
    if num == 2:
        return True
    limit = sqrt(num)
    index = 2
    while index <= limit:
        if num % index == 0:
            return False
        index += 1
    return True


def generate_question_and_answer():
    """Generate question and answer.

    Returns:
            retruns - tuple of question and answer
    """
    START_OF_RANGE = 1
    END_OF_RANGE = 100
    num = randint(START_OF_RANGE, END_OF_RANGE)
    if is_prime(num):
        answer = 'yes'
    else:
        answer = 'no'
    return (str(num), answer)
