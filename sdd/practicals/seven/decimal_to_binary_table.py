#!/usr/bin/env python3

"""

    Prints the decimals from 0 to 127 with their 8 bit binary equivalent.

"""

__author__ = "Aspen Thompson"
__email__ = "u1862679@hud.ac.uk"
__date__ = "2018-11-8"

if __name__ == "__main__":
    for i in range(0, 128):
        print("{0:3} {0:08b}".format(i))
