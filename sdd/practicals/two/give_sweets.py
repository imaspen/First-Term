def get_input(thing):
    while True:
        response = input("How many %s are there? " % thing)
        try:
            return int(response)
        except ValueError:
            print("Please enter a whole number.")


def get_value(thing):
    response = get_input(thing)
    while response <= 0:
        print("Please enter a value greater than 0.")
        response = get_input(thing)
    return response


number_of_pupils = get_value("pupils")
number_of_sweets = get_value("sweets")

print("Sweets per pupil: " + str(number_of_sweets // number_of_pupils))
print("Sweets left over: " + str(number_of_sweets % number_of_pupils))

