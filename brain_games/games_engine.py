# -*- coding:utf-8 -*-

"""engine of games."""


from brain_games import cli


def start_games(game_name):
    """Start engin of games.

    Args:
        game_name: name of game

    """
    NUM_OF_ROUND = 3
    user_name = cli.welcome_user()
    print(game_name.ASK_STR)
    for _ in range(0, NUM_OF_ROUND):
        question, correct_answer = game_name.generate_question_and_answer()
        answer = cli.ask_question(question)
        if correct_answer != answer:
            wrong_answer = "\'{0}\' is wrong answer ;(.".format(answer)
            correct_answer = "Correct answer was \'{0}\'".format(correct_answer)
            print('{0} {1}.'.format(wrong_answer, correct_answer))
            print("Let\'s try again, {0}!".format(user_name))
            return
        print('Correct!')
    # Поздравления
    print('Congratulations, {0}!'.format(user_name))
