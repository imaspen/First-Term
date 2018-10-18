"""
Takes a users name and greets them

AT
11-10-2018
"""

name = input("Hello, who are you? ").capitalize()

if len(name) > 0:
    if name == "Arthur":
        print("My Liege! It is good to meet you.")
    else:
        print("Hello, Sir {0}. It is good to meet you.".format(name))
else:
    print("Hello World.")
