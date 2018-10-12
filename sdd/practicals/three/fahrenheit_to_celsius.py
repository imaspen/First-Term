"""
Gets a temperature in fahrenheit and converts it to celsius

AT
11-10-2018
"""


def get_temperature():
    """Gets the temperature as a float from the user."""
    while True:
        try:
            temperature = float(input("Enter the temperature in fahrenheit: "))
            return temperature
        except ValueError:
            print("Please enter a number.")


celsius = (get_temperature() - 32) * 1.8

print("Temperature in celsius:", celsius)
