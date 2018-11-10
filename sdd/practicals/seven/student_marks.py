Number_of_Results = 5

results = []

for count in range(Number_of_Results):
    while 1:
        result = int(input("Enter result #" + str(count+1) + ": "))
        if result in range(0,101):
            results.append(result)
            break
        else:
            print("Invalid. Try again.")

print("Average is: ", sum(results) / len(results))
