"""This file add at step three"""

import prompt

def welcome_user():
    """Welcome user. Ask his name and print"""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
