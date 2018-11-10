#!/usr/bin/env python3

"""

    Takes a football team's name and last 5 results, and displays games won, drawn,
    lost, and the points earned by the team.

"""

__author__ = "Aspen Thompson"
__email__ = "u1862679@hud.ac.uk"
__date__ = "2018-11-08"


def get_goals(prompt, match):
    while 1:
        try:
            goals = int(input("Goals {} in Match #{}: ".format(prompt, match)))
            if goals >= 0:
                return goals
            else:
                print("Please enter a positive number")
        except ValueError:
            print("Please enter an integer.")


if __name__ == "__main__":
    team = input("Enter the Team Name: ")

    # A list storing [wins, draws, losses].
    results = [0, 0, 0]
    for i in range(1, 6):
        result = (get_goals("Scored", i), get_goals("Against", i))
        if result[0] > result[1]:
            results[0] += 1
        elif result[0] == result[1]:
            results[1] += 1
        else:
            results[2] += 1

    print("{}\nWins:   {}\nDraws:  {}\nLosses: {}\nPoints: {}".format(
        team, results[0], results[1], results[2], results[0] * 3 + results[2]
    ))
