#!/bin/bash
# Aspen Thompson
# u1862679@hud.ac.uk
# v1.0.0
# 2018-12-14
# List the contents and size of each file within the wastebin

# Make waste directory if it does not exist.
mkdir -p ~/.waste

# If waste contains files, move to the waste directory, output bytes for each file, then move back.
if [ "$(ls -A ~/.waste)" ]; then
	# Output templating
	echo -e "Size\tFile Name"
	cd ~/.waste/
    # Get output of wc bytes count, trim leading spaces, and replace middle space with a tab.
	wc -c * | awk '{$1=$1};1' | tr ' ' \\t
	cd - > /dev/null
else
	echo "Waste is empty."
fi
