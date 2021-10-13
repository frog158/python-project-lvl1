#!/usr/bin/env python3
"""Project One. Brain calc."""

from brain_games import games_engine
from brain_games.games import calc


def main():
    """Let's start the calc game."""
    games_engine.start_games(calc)


if __name__ == '__main__':
    main()
