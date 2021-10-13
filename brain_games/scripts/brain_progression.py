#!/usr/bin/env python3
"""Project One. Brain Progression."""

from brain_games import games_engine
from brain_games.games import progression


def main():
    """Let's start the progression game."""
    games_engine.start_games(progression)


if __name__ == '__main__':
    main()
