#!/usr/bin/env python3

"""

    Contains functions for questions 1 - 4.

"""
import random

__author__ = "Aspen Thompson"
__email__ = "u1862679@hud.ac.uk"
__date__ = "15-11-2018"


def random_answer():
    """Returns a random string from a list."""
    ANSWERS = ['Yes', 'No', 'Maybe', 'Ni!']
    return random.choice(ANSWERS)


if __name__ == "__main__":
    pass
