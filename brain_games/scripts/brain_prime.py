#!/usr/bin/env python3
"""Project One. Brain Prime."""

from brain_games import games_engine
from brain_games.games import prime


def main():
    """Let's start the Prime game."""
    games_engine.start_games(prime)


if __name__ == '__main__':
    main()
