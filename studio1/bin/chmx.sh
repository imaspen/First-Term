#!/bin/bash
# Aspen Thompson
# u1862679@hud.ac.uk
# v1.0.0
# 2018-12-14
# Make a file executable

# If we were passed an argument that is a file and not a directory
if (( $#==1 )) && [[ -e $1 ]] && [[ ! -d $1 ]]; then
    # Run the chmod command, with the all + executable command, passing the first argument.
    chmod a+x "$1"
else
    echo "Error, no file given."
    echo "Usage: chmx [file]"
    exit 1
fi

