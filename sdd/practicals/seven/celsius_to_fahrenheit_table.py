"""
Generates a temperature celsius to fahrenheit conversion table

AT
11-10-2018
"""

__author__ = "Aspen Thompson"

header = "| Celsius | Fahrenheit |"
line = "-" * len(header)
print("{0}\n{1}\n{0}".format(line, header))

for i in range(-10, 31):
    print("| {:^7} | {:^10.10} |".format(i, i * 1.8 + 32))

