"""
Gets a temperature in celsius and converts it to fahrenheit

AT
11-10-2018
"""


def get_temperature():
    """Gets the temperature as a float from the user."""
    while True:
        try:
            temperature = float(input("Enter the temperature in celcius: "))
            return temperature
        except ValueError:
            print("Please enter a number.")


fahrenheit = get_temperature() * 1.8 + 32

print("Temperature in fahrenheit:", fahrenheit)
