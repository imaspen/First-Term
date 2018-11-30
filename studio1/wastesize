#!/bin/bash

# Make the waste directory if it does not yet exist.
mkdir -p ~/.waste

# Get the number of lines in the waste directory that are not directories of symlinks. 
lines=$(ls -l ~/.waste | grep -c ^-)

echo "Files in waste:" $lines

