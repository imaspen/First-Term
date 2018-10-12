"""
Takes a users name and greets them

AT
11-10-2018
"""

name = input("Hello, who are you? ")

if len(name) > 0:
    print("Hello, {0}. It is good to meet you.".format(name))
else:
    print("Hello World.")
