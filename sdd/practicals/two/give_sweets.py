"""
Gets the number of sweets a teacher has, and tells them how many to give each pupil to split them evenly.

AT
04-10-18
"""


def get_input(thing):
    """Ask the user to enter a whole number of things and return it"""
    while True:
        response = input("How many %s are there? " % thing)
        try:
            return int(response)
        except ValueError:
            print("Please enter a whole number.")


def get_value(thing):
    """Get a positive non-zero value of things from a user and return it"""
    response = get_input(thing)
    while response <= 0:
        print("Please enter a value greater than 0.")
        response = get_input(thing)
    return response


# Get input
number_of_pupils = get_value("pupils")
number_of_sweets = get_value("sweets")

# Print output
print("Sweets per pupil: " + str(number_of_sweets // number_of_pupils))
print("Sweets left over: " + str(number_of_sweets % number_of_pupils))

