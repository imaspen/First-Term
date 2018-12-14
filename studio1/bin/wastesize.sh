#!/bin/bash
# Aspen Thompson, u1862679@hud.ac.uk
# Gets the number of files in the waste directory

# Make the waste directory if it does not yet exist.
mkdir -p ~/.waste

# Get the number of lines in the waste directory that are not directories of symlinks. 
lines=$(ls -l ~/.waste | grep -c ^-)

echo "Files in waste:" $lines

