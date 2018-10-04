number_of_pupils = int(input("How many pupils are there? "))
number_of_sweets = int(input("How many sweets are there? "))

print("Sweets per pupil: " + str(number_of_sweets // number_of_pupils))
print("Sweets left over: " + str(number_of_sweets % number_of_pupils))

