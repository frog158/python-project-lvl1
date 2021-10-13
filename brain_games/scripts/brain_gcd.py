#!/usr/bin/env python3
"""Project One. Brain GDC."""

from brain_games import games_engine
from brain_games.games import gcd


def main():
    """Let's start the GCD game."""
    games_engine.start_games(gcd)


if __name__ == '__main__':
    main()
