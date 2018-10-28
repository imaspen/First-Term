"""
Take a number of students and computers per lab, and return how many labs are needed.

AT
28/10/18
"""
import math


def get_int(prompt):
    entered = 0
    while True:
        try:
            entered = int(input("Enter the number of {0}: ".format(prompt)))
            if entered > 0:
                return entered
            print("Please enter a number greater than 0.\n")

        except:
            print("Please enter an integer.")


if __name__ == "__main__":
    students = get_int("students in the class")
    computers = get_int("PCs in the lab")

    labs_needed = math.ceil(students / computers)

    lab_string = "lab"
    if labs_needed > 1:
        lab_string += "s"

    student_string = "the student"
    if students > 1:
        student_string = "all {0}s".format(student_string)

    print("You need {0} {1} for {2}.".format(
        labs_needed, lab_string, student_string
    ))
