def get_number(thing):
    while True:
        response = input("How many %s are there? " % thing)
        try:
            return int(response)
        except ValueError:
            print("Please enter a whole number.")


number_of_pupils = get_number("pupils")
number_of_sweets = get_number("sweets")

while number_of_pupils <= 0:
    print("You can't give something to no one.")
    number_of_pupils = get_number("pupils")

while number_of_sweets <= 0:
    print("You can't give them nothing.")
    number_of_sweets = get_number("sweets")

print("Sweets per pupil: " + str(number_of_sweets // number_of_pupils))
print("Sweets left over: " + str(number_of_sweets % number_of_pupils))

