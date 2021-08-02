#! /bin/bash
# Script Name:      Directory Director
# Author:           marburgja
# Last Rev:         20210802
# Purpose:          Finds a dir, or creates a new dir

# Variables
listem="ls"

# Functions
dirmaker(){
    for item in $listem
    do
        mkdir $dirname
    done
}

# Main
$listem
read dirname
if [[ ! -e ./$dirname ]]
then
    dirmaker
else
    echo "That's already there!"
fi
    
# End