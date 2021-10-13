# -*- coding:utf-8 -*-

"""Gdc game."""


from random import randint

ASK_STR = 'Find the greatest common divisor of given numbers.'


def find_gcd(x1, x2):
    """Find the gdc of.

    Args:
        x1: one
        x2: two

    Returns:
        returns: gcd of two integer
    """
    while x1 != 0 and x2 != 0:
        if x1 > x2:
            x1 %= x2
        else:
            x2 %= x1
    return (x1 + x2)


def generate_question_and_answer():
    """Generate question and answer.

    Returns:
            retruns - tuple of question and answer
    """
    START_OF_RANGE = 1
    END_OF_RANGE = 100
    x1 = randint(START_OF_RANGE, END_OF_RANGE)
    x2 = randint(START_OF_RANGE, END_OF_RANGE)
    answer = find_gcd(x1, x2)
    return ('{0} {1}'.format(str(x1), str(x2)), str(answer))
