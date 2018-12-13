#!/bin/bash
# Aspen Thompson, u1862679@hud.ac.uk
# Removes everything from the wastebin, including the wastebin directory

# Attempt to remove the waste directory and it's contents, suppressing errors if it does not exist.
rm -rf ~/.waste
