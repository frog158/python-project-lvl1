"""This file add at step three."""

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
