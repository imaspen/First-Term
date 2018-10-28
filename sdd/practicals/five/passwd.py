"""
Takes a password twice and returns a message if they match.

AT
28/10/18
"""


def get_string(again = ""):
    return input("Enter new password{0}: ".format(again))


if __name__ == "__main__":
    password = get_string()
    if 6 <= len(password) <= 12:
        if password == get_string(" again"):
            print("Password changed.")
        else:
            print("Passwords do not match.")
    else:
        print("Password must be between 6 and 12 characters long.")
