"""
Takes any number of temperature readings and displays the highest, lowest, and average reading.

AT
11-10-2018
"""


readings = []
while True:
    try:
        readings.append(float(input("Enter a temperature reading or anything other than a number to finish: ")))
    except ValueError:
        break


readings.sort()
highest_temp = readings[-1]
lowest_temp = readings[0]
average_temp = sum(readings) / len(readings)

print("Highest temp: {0}, lowest temp: {1}, average temp: {2}.".format(
    highest_temp, lowest_temp, average_temp
))
