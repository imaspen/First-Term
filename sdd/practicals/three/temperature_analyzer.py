"""
Takes 4 temperature readings and displays the highest, lowest, and average reading.

AT
11-10-2018
"""


def get_reading(number):
    """Gets the nth reading from the user and returns it as a float"""
    while True:
        try:
            temperature = float(input("Enter temperature reading {0}: ".format(number)))
            return temperature
        except ValueError:
            print("Please enter a number.")


readings = []
for i in range(1, 5):
    readings.append(get_reading(i))

readings.sort()
highest_temp = readings[-1]
lowest_temp = readings[0]
average_temp = sum(readings) / len(readings)

print("Highest temp: {0}, lowest temp: {1}, average temp: {2}.".format(
    highest_temp, lowest_temp, average_temp
))
