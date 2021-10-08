# -*- coding:utf-8 -*-

"""Even game."""


from random import randint

import prompt


def welcome_user():
    """Welcome user fuction.

    Ask his name and print.

    Returns:
        string: User Name.

    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    return user_name


def correct():
    """Print if answer is correct."""
    print('Correct!')


def incorrect(user_name, user_answer, correct_answer):
    """Print if answer is incorect.

    Args:
        user_name: User name.
        user_answer: User answer.
        correct_answer: Correct answer.

    """
    wrong_answer = "\'{0}\' is wrong answer ;(.".format(user_answer)
    correct_answer = "Correct answer was \'{0}\'".format(correct_answer)
    print("{0} {1}\'.".format(wrong_answer, correct_answer))
    print("Let\'s try again, {0}!".format(user_name))


def check_answer(number, answer):
    """Check answer for yes or no. And check.

    Args:
        number: the number.
        answer: the answer.

    Returns:
        integer: if answer correct 0, if incorect 1

    """
    correct_answer = ''
    if (number % 2) == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    if (answer not in {'yes', 'no'}) or (correct_answer != answer):
        return (1, correct_answer)
    return (0, correct_answer)


def ask_answer():
    """В этой функции задаем вопрос и получаем ответ.

    Returns:
        Returns tuple - asked question and user answer

    """
    question = randint(1, 100)
    print('Question: {0}'.format(question))
    answer = prompt.string('Your answer: ')
    check_result, correct_answer = check_answer(question, answer)
    return (answer, check_result, correct_answer)


def start_game():
    """Even game."""
    user_name = welcome_user()
    index = 1
    while index <= 3:
        answer, check_result, correct_answer = ask_answer()
        if check_result == 1:
            incorrect(user_name, answer, correct_answer)
            return
        correct()
        index += 1
    # Поздравления
    print('Congratulations, {0}!'.format(user_name))
