"""
Takes a password twice and returns a message if they match.

AT
28/10/18
"""


def get_string(again = ""):
    return input("Enter new password{0}: ".format(again))


if __name__ == "__main__":
    if get_string() == get_string(" again"):
        print("Password changed.")
