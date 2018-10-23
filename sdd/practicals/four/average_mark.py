name = input("Enter the student's name: ")

mark_1 = int(input("Enter the first result: "))
mark_2 = int(input("Enter the second result: "))
mark_3 = int(input("Enter the third result: "))
mark_4 = int(input("Enter the fourth result: "))
mark_5 = int(input("Enter the fifth result: "))

total_marks = mark_1 + mark_2 + mark_3 + mark_4 + mark_5

average_mark = total_marks / 5

print()
print("Final mark for {0} is {1}.".format(name, average_mark))
