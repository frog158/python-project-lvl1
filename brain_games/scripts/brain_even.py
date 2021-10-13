#!/usr/bin/env python3
"""Project One. Brain even."""

from brain_games import games_engine
from brain_games.games import even


def main():
    """Let's start the even game."""
    games_engine.start_games(even)


if __name__ == '__main__':
    main()
