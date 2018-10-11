"""
Gets the length of 2 sides of a rectangle, then returns the area

AT
11-10-2018
"""


def get_side(side):
    """Gets the length of a side as a float from the user."""
    while True:
        try:
            length = float(input("Enter length of side {0}: ".format(side)))
            if length > 0:
                return length
            else:
                print("Please enter a length greater than 0.")
        except ValueError:
            print("Please enter a number.")


area = get_side(1) * get_side(2)

print("Rectangle area:", area)
