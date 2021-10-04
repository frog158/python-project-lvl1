# -*- coding:utf-8 -*-

"""engine of games."""


import prompt


def welcome_user(ask_string):
    """Welcome user fuction.

    Ask his name and print.

    Args:
        ask_string: question in the game

    Returns:
        string: User Name.

    """
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user_name))
    print(ask_string)
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


def ask_question(question):
    """In this function ask the question.

    Args:
        question: User question.

    Returns:
        Returns - user answer

    """
    print('Question: {0}'.format(question))
    return prompt.string('Your answer: ')


def start_engine(ask_str, list_of_question):
    """Start engin of games.

    Args:
        ask_str: string with questinon
        list_of_question: list of tuple.

    """
    user_name = welcome_user(ask_str)
    index = 0
    while index < 3:
        question, correct_answer = list_of_question[index]
        answer = ask_question(question)
        if correct_answer != answer:
            incorrect(user_name, answer, correct_answer)
            return
        correct()
        index += 1
    # Поздравления
    print('Congratulations, {0}!'.format(user_name))
