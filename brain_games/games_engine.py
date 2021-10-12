# -*- coding:utf-8 -*-

"""engine of games."""


import prompt
from brain_games.games import calc, even, gcd, prime, progression


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


def incorrect(user_name, user_answer, correct_answer):
    """Print if answer is incorect.

    Args:
        user_name: User name.
        user_answer: User answer.
        correct_answer: Correct answer.

    """
    wrong_answer = "\'{0}\' is wrong answer ;(.".format(user_answer)
    correct_answer = "Correct answer was \'{0}\'".format(correct_answer)
    print('{0} {1}.'.format(wrong_answer, correct_answer))
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
    for question, correct_answer in list_of_question:
        answer = ask_question(question)
        if correct_answer != answer:
            incorrect(user_name, answer, correct_answer)
            return
        print('Correct!')
    # Поздравления
    print('Congratulations, {0}!'.format(user_name))


def get_list_question(generate):
    """Generate list of question.

    Args:
        generate: function which generate question

    Returns:
        returns - list of question
    """
    NUM_OF_ROUND = 3
    list_of_question = []
    for _ in range(0, NUM_OF_ROUND):
        list_of_question.append(generate())
    return list_of_question


def start_games(name_of_game):
    """Root function of all games.

    Args:
        name_of_game: string name of games

    """
    games_function = ([
        ('calc', calc.generate_question, calc.get_start_msg),
        (
            'progression',
            progression.generate_question,
            progression.get_start_msg,
        ),
        ('prime', prime.generate_question, prime.get_start_msg),
        ('gcd', gcd.generate_question, gcd.get_start_msg),
        ('even', even.generate_question, even.get_start_msg),
    ])
    for name, generate, get in games_function:
        if name == name_of_game:
            start_engine(get(), get_list_question(generate))
            break
