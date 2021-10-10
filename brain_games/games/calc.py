# -*- coding:utf-8 -*-

"""Calc game."""


from random import choice, randint


def get_operand():
    """Generate operand.

    Returns:
        return - operand
    """
    START_OF_RANGE = 1
    END_OF_RANGE = 100
    return (randint(START_OF_RANGE, END_OF_RANGE))


def get_question():
    """Generate two operands and operator.

    Returns:
        return - tuple operands and operator
    """
    OPERATOR_LIST = ['+', '-', '*']
    x1 = get_operand()
    x2 = get_operand()
    operator_string = choice(OPERATOR_LIST)
    return (x1, x2, operator_string)


def generate_question():
    """Generate question and answer.

    Returns:
            retruns - tuple of question and answer
    """
    x1, x2, operator_string = get_question()
    if operator_string == '+':
        answer = str(x1 + x2)
    elif operator_string == '-':
        answer = str(x1 - x2)
    else:
        answer = str(x1 * x2)
    return ('{0} {2} {1}'.format(str(x1), str(x2), operator_string), answer)


def get_start_msg():
    """Return start message.

    Returns:
        returns - string. Start message
    """
    return 'What is the result of the expression?'
