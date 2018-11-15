#!/usr/bin/env python3

"""

    Contains functions for questions 1 - 4.

"""
import random
import re

__author__ = "Aspen Thompson"
__email__ = "u1862679@hud.ac.uk"
__date__ = "15-11-2018"


def random_answer():
    """Returns a random string from a list."""
    ANSWERS = ['Yes', 'No', 'Maybe', 'Ni!']
    return random.choice(ANSWERS)


def is_email(candidate):
    """
    Checks a string to check if it is a valid email address.
    Parameters: potential email
    Returns: True if email, False otherwise
    """
    email_check = re.compile("\A[\w_.]+@[\w.]+\.[a-zA-Z]+\Z")
    return email_check.match(candidate)


if __name__ == "__main__":
    pass
