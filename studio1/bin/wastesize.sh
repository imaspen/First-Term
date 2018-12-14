#!/bin/bash
# Aspen Thompson
# u1862679@hud.ac.uk
# v1.0.0
# 2018-12-14
# Gets the number of files in the waste directory

# Make the waste directory if it does not yet exist.
mkdir -p ~/.waste

# Get the number of lines in the waste directory that are not directories of symlinks. 
lines=$(ls -l ~/.waste | grep -c ^-)

echo "Files in waste:" $lines

