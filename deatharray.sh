#! /bin/bash
# Script Name:      Death Array
# Author:           marburgja
# Last Rev:         20210729
# Purpose:          Create 4 directories and create a file in each directory

# Variables
creator="mkdir dir1 dir2 dir3 dir4"
creations=("dir1" "dir2" "dir3" "dir4")

# Functions
deatharray(){
   for item in ${creations[@]}
   do
       touch ./$item/subcreations.txt
   done
}

# Main
$creator
deatharray


# End