# -*- coding:utf-8 -*-

"""Even game."""


from random import randint


def generate_question():
    """Generate question and answer.

    Returns:
            retruns - tuple of question and answer
    """
    START_OF_RANGE = 1
    END_OF_RANGE = 100
    num = randint(START_OF_RANGE, END_OF_RANGE)
    answer = 'no'
    if num % 2 == 0:
        answer = 'yes'
    return (num, answer)


def get_start_msg():
    """Return start message.

    Returns:
        returns - string. Start message
    """
    return 'Answer "yes" if the number is even, otherwise answer "no".'
