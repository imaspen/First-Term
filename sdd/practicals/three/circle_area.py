"""
Gets the radius a circle, then returns the area.

AT
11-10-2018
"""
from math import pi


def get_radius():
    """Gets the radius as a float from the user."""
    while True:
        try:
            radius = float(input("Enter the radius of the circle: "))
            if radius > 0:
                return radius
            else:
                print("Please enter a radius greater than 0.")
        except ValueError:
            print("Please enter a number.")


area = pi * (get_radius() ** 2)

print("Cirle area:", area)
