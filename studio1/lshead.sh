#!/bin/bash

# Setup variables to be used in the final command.
mode="head"
count=10
recursive=false
directory=.

# For each passed argument, change the relevant variable.
while (( $# )); do
    if [[ "$1" = "--help" ]]; then
        echo "Prints the first or last lines of files in a directory."
        echo "Usage: lshead [[--head|--tail] count] [--recursive] [directory]"
        echo "Options:"
        echo -e "\t-h, --head:\t\tview the first lines"
        echo -e "\t-t, --tail:\t\tview the last lines"
        echo -e "\t-r, --recursive:\tview files in subdirectories"
        exit 1
    elif [[ "$1" =~ ^((-r)|(--recursive))$ ]]; then
        recursive=true
    elif [[ "$1" =~ ^((-t)|(--tail))$ ]]; then
        mode="tail"
        shift
        count="$1"
    elif [[ "$1" =~ ^((-h)|(--head))$ ]]; then
        mode="head"
        shift
        count="$1"
    elif [[ "$1" =~ ^((-d)|(--directory))$ ]]; then
        shift
        if [[ -d $1 ]]; then
            directory=$1
        else
            echo "Invalid directory given."
            exit 1
        fi
    else
        echo "Unrecognized argument: $1"
        echo "Use lshead --help for more info."
        exit 1
    fi
    shift
done

# Get all files from the given directory.
for file in $directory/*; do
    if [[ ! -d $file ]]; then
        # If file is not a directory, output it's name and run the chosen command.
        echo -e "\n## $file ##\n"
        $mode -n$count $file
    elif [[ $recursive = "true" ]]; then
        # If file is a directory and recursive flag was set, run the script again from the directory.
        echo -e "\n#### $file ####"
        ./$0 --directory $file --$mode $count
    fi
done

