#! /bin/bash
# Script Name:      Directory Director
# Author:           marburgja
# Last Rev:         20210802
# Purpose:          Finds a dir, or creates a new dir

# Variables
listem=ls

# Functions
dirmaker(){
    until [ -e ./$dirname ]
    do
        mkdir $dirname
    done
}

# Main
$listem
echo "Enter New Directory Name:"
read dirname
if [[ ! -e ./$dirname ]]
then
    dirmaker
else
    echo "That's already there!"
fi
    
# End