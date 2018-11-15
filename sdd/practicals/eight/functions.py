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
    :param candidate: the potential email address.
    :return: True if is an email address, else False.
    """
    email_check = re.compile("\A[^@\s]+@[^@\s]+\.[^@\s]+\Z")
    return email_check.match(candidate)


def get_email_user(email_address):
    """
    Gets all of an email address that precedes the @.
    :param email_address: the email address to strip.
    :return: the string that precedes the @.
    """
    return email_address[:email_address.find("@")]


def get_ni_input():
    """
    Asks the user to enter text until "Ni!" is entered, regardless of case.
    :return: nothing.
    """
    while True:
        if input("Enter a string: ").lower() == "ni!":
            print("You may pass!")
            return
        else:
            print("Bring me a shrubbery!")


if __name__ == "__main__":
    pass
