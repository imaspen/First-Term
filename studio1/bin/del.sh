#!/bin/bash
# Aspen Thompson, u1862679@hud.ac.uk
# Moves a file to a wastebin

# Make the waste directory in the users home directory if it does not exist.
mkdir -p ~/.waste

# Test if we are attempting to delete a file.
if [[ -e "$1" ]]; then
    # Test if we are attempting to delete a directory.
    if [[ -d "$1" ]]; then
        echo "Cannot delete $1: Is a directory."
	    exit 1
    else
        mv "$1" ~/.waste
    fi
else
    echo "Please give a file to delete."
    exit 1
fi

