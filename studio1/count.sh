#!/bin/bash

# Check if the help command or no input was passed and give help.
if [[ "$1" == "--help" ]] || [[ "$1" == "-h" ]] || [[ "$1" == "" ]]; then
	echo "Takes an argument, and asks for more input until a control character (*) is entered."
	echo "Outputs the count of letters, digits, and other characters entered."
	exit 0
fi

# Set done flag, 1st argument as string to analyze, and counting variable.
done=false
input="$@"
letters=0
digits=0
other=0

# Start an infinite loop.
while true; do
	# For each character in input, increment the relevant counter, and exit on the control character.
	for (( i=0; i<${#input}; i++ )); do
		char=${input:$i:1}
		if [[ "$char" =~ [a-zA-Z] ]]; then
			((letters++))
		elif [[ "$char" =~ [0-9] ]]; then
			((digits++))
		else
			((other++))
			if [[ "$char" == "*" ]]; then
				done=true
				break		
			fi
		fi
	done

	# If flag is set (control character was entered), break out of the infinite loop.
	if [[ $done == true ]]; then
		break
	fi

	# Ask the user for more input.
	echo -n "Input a string or enter * to finish: "
	read input
done

# Output the counters.
echo "Total length:" $((letters+digits+other))
echo "Letters input:" $letters
echo "Digits input:" $digits
echo "Other characters (including control character):" $other
