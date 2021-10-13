# -*- coding:utf-8 -*-

"""Calc game."""


from random import choice, randint

ASK_STR = 'What is the result of the expression?'


def get_question():
    """Generate two operands and operator.

    Returns:
        return - tuple operands and operator
    """
    START_OF_RANGE = 1
    END_OF_RANGE = 100
    OPERATOR_LIST = ['+', '-', '*']
    x1 = randint(START_OF_RANGE, END_OF_RANGE)
    x2 = randint(START_OF_RANGE, END_OF_RANGE)
    operator_string = choice(OPERATOR_LIST)
    return (x1, x2, operator_string)


def calculate_expression(operand_1, operand_2, operator):
    """Calculate expression.

    Args:
        operand_1: operand 1
        operand_2: operand 2
        operator: operator

    Returns:
        Return: answer - integer result of expression
    """
    if operator == '+':
        answer = str(operand_1 + operand_2)
    elif operator == '-':
        answer = str(operand_1 - operand_2)
    else:
        answer = str(operand_1 * operand_2)
    return answer


def generate_question_and_answer():
    """Generate question and answer.

    Returns:
            retruns - tuple of question and answer
    """
    x1, x2, operator_string = get_question()
    answer = calculate_expression(x1, x2, operator_string)
    return ('{0} {2} {1}'.format(str(x1), str(x2), operator_string), answer)
