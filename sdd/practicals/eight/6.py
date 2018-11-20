#!/usr/bin/env python3

"""

    Simulates a chat system for a University.

"""
import random
import re

__author__ = "Aspen Thompson"
__email__ = "u1862679@hud.ac.uk"
__date__ = "15-11-2018"


def get_random_name():
    """
    Returns a random string from a list.
    :return: name string
    """
    NAMES = ['Alice', 'Bob', 'Charlie', 'Delia']
    return random.choice(NAMES)


def get_random_answer():
    """
    Returns a random answer from a list.
    :return: answer string
    """
    ANSWERS = ["Maybe.", "Tell me more.", "I am pleased to hear that."]
    return random.choice(ANSWERS)


def is_valid_email(candidate):
    """
    Checks a string to check if it is a valid email address.
    :param candidate: the potential email address.
    :return: True if is an email address, else False.
    """
    email_check = re.compile("\A[^@\s]+@pop\.ac\.uk\Z")
    return email_check.match(candidate)


def get_email_user(email_address):
    """
    Gets all of an email address that precedes the @.
    :param email_address: the email address to strip.
    :return: the string that precedes the @.
    """
    return email_address[:email_address.find("@")].capitalize()


def get_query_input():
    """
    Asks the user to enter text until "goodbye" is entered.
    :return: nothing.
    """
    while True:
        query = input("Please enter your query: ").lower()

        if question_has_string(query, "library"):
            print("The library is closed today.")
        elif question_has_string(query, "wifi"):
            print("WiFi is excellent across the campus.")
        elif question_has_string(query, "deadline"):
            print("Your deadline has been extended by two working days.")
        elif query == "goodbye":
            print("Goodbye!")
            return
        else:
            print(get_random_answer())

        if random.randint(0, 100) < 15:
            print("Connection Lost")
            return


def question_has_string(question, search_string):
    """
    Checks if a string is within a question.
    :param question: the string to search within
    :param search_string: the string to search for
    :return: True if question has string, else False
    """
    return search_string in question


if __name__ == "__main__":
    email = input("Please enter your University of Poppleton email address: ")
    if is_valid_email(email):
        print("Thank you, that email checks out.")
    else:
        print("That email is not valid, sorry, but we will be unable to answer your query, goodbye.")
        exit(1)

    print("Hello {}, my name is {}.".format(get_email_user(email), get_random_name()))

    get_query_input()
