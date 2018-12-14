#!/bin/bash
# Aspen Thompson
# u1862679@hud.ac.uk
# v1.0.0
# 2018-12-14
# Takes an input file extension and changes all files to another extension.

info_string="For more info, use chext --help"

# Set argument defaults
current=''
new=''
dir=.
all_flag=false
strip_flag=false

# If no arguments given or the help switch given, give help and exit
if (( $#==0 )) || [[ "$1" =~ ^((-h)|(--help))$ ]]; then
    echo "chext: Changes all files of one extension to another."
    echo "Usage: chext [-d dir] [in|-a] [out|-s]"
    echo -e "\t-d:\tset the directory to change file extensions, defaults to ."
    echo -e "\t-a:\tchanges the extension for all files"
    echo -e "\t-s:\tremoves file extensions"
    exit 1
fi

# Handle each arg
while (( $# )); do
	if [[ "$1" =~ ^((-d)|(--directory))$ ]]; then
		shift
        if [[ -d $1 ]]; then
            dir=$1
        else
            echo "Invalid directory given"
            echo $info_string
            exit 1
        fi
    elif [[ "$1" =~ ^((-a)|(--all))$ ]]; then
        all_flag=true
    elif [[ "$1" =~ ^((-s)|(--strip))$ ]]; then
        strip_flag=true
	elif [[ $current = '' ]] && [[ $all_flag = false ]]; then
		current="$1"
	elif [[ $new = '' ]] && [[ $strip_flag = false ]]; then
        new="$1"
        if [[ "${new:0:1}" != "." ]]; then
            new=".$new"
        fi
	fi
    shift
done

# Handle too few args
if [[ $current = '' ]] && [[ $all_flag = false ]]; then
    echo "Please give an input file extension, or use -a to select all."
    echo $info_string
    exit 1
elif [[ $new = '' ]] && [[ $strip_flag = false ]]; then
    echo "Please enter an output file extension, or use -s to remove extensions."
    echo $info_string
    exit 1
fi

# Move to target directory, rename each file, and move back
cd $dir

if [[ $all_flag ]]; then
    for file in *; do
        if [[ ! -d $file ]]; then
            mv "$file" "${file%.*}$new"
        fi 
    done
else
    for file in *.$current; do
        if [[ ! -d $file ]]; then
            mv "$file" "${file%.$current}$new"
        fi
    done
fi

cd - > /dev/null

