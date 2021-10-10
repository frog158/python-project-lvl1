# -*- coding:utf-8 -*-

"""Progression game."""


from math import sqrt
from random import randint


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


def generate_question():
    """Generate question and answer.

    Returns:
            retruns - tuple of question and answer
    """
    START_OF_RANGE = 1
    END_OF_RANGE = 100
    num = randint(START_OF_RANGE, END_OF_RANGE)
    answer = is_prime(num)
    return (str(num), answer)


def get_start_msg():
    """Return start message.

    Returns:
        returns - string. Start message
    """
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'
