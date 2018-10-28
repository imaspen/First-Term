"""
Takes a password twice and returns a message if they match and follow password rules.

AT
28/10/18
"""

import string
import random


def get_string(prompt):
    return input("Enter {0}: ".format(prompt))


def get_password():
    """Prompts the user to enter a new password until it passes given criteria, and prints password changed."""
    username = get_string("username")
    student_id = get_string("student ID")

    banned = ["huddersfield", "justinbieber", "cheese", "canalside"]

    while True:
        password = get_string("new password")

        if len(password) < 6 or len(password) > 12:
            print("Password must be between 6 and 12 characters long.")
        elif password == username:
            print("Password cannot be your username.")
        elif password == student_id:
            print("Password cannot be your student ID.")
        elif password in banned:
            print("Common passwords cannot be used.")
        elif password != get_string("new password again"):
            print("Entered passwords must match.")
        else:
            print("Password changed.")
            break
        print()


def random_password():
    characters = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    password = ''
    for i in range(0, 16):
        password += random.choice(characters)

    print("Generated password: " + password)


if __name__ == "__main__":
    mode = ''
    while mode not in ['r', 'c']:
        mode = input("Would you like a (r)andom or (c)ustom password? ")[0]

    if mode == 'c':
        get_password()
    else:
        random_password()
