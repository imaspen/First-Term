#!/bin/bash

# Shortcuts a number of git tasks.

# Give help
function giveHelp {
    echo "Adds shortcuts for common git tasks."
    echo "Usage: agit [mode] [file] [message]"
    echo "Modes:"
    echo -e "\tadd:\tcommits a file to the repo."
    echo -e "\tbranch:\tcreates a new branch from the latest master."
    echo -e "\trevert:\tundo all changes to files since the last commit."
    exit 1
}

# Commit a file
function addFile {
    # if the file exists
    if [[ -e $1 ]]; then
        # make sure its the only file staged
        git reset > /dev/null
        git add $1

        # find if the file is new, changed, or unchanged, and set message accordingly
        file_status=$(git status | grep $1)
        message=""
        if (( $(echo $file_status | grep "modified" | wc -l) > 0 )); then
            message="updated $1"
        elif (( $(echo $file_status | grep "new file" | wc -l) > 0 )); then
            message="created $1"
        else
            echo "No changes detected."
            exit 1
        fi

        shift

        # append a custom message and commit
        if [[ $1 != "" ]]; then
            message="$message: $@"
        fi

        git commit -m "$message"
        git push
    fi
}

# Create a new branch from master
function createBranch {
    # if name is given, checkout master, make sure it is up to date, and create a new branch
    if [[ $1 != "" ]]; then
        git checkout master
        git pull
        git checkout -b $1
    else
        echo "No branch name given.\nUse agit -h for more info."
        exit 1
    fi
}

# Undo changes made to a file since last commit
function revertChanges {
    if [[ -e $1 ]]; then
        if (( $(git status | grep $1 | wc -l) > 1 )); then
            git checkout HEAD -- $1
            echo "Changes to file reverted."
        else
            echo "No changes have been made to the file."
            exit 1
        fi
    else
        echo "File doesn't exist to reset."
        exit 1
    fi
}

# Handle user input
case "$1" in
    help | --help | -h)
        giveHelp
    ;;
    add | a)
        shift
        addFile "$@" 
    ;;
    branch | b)
        createBranch $2
    ;;
    revert | r)
        revertChanges $2
    ;;
    *)
        echo -e "Command not recognized.\nUse agit -h for more info."
        exit 1
    ;;
esac

