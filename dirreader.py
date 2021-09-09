#! /usr/bin/env python3
# Script Name:      dirreader
# Author:           marburgja
# Last Rev:         20210908
# Purpose:          generates all directories, sub-directories, and files for a provide path

# Libraries
import os

# Variables
path=input("Please Enter Filepath:")

# Functions
def dirreader():
    for (root, dirs, files) in os.walk(path):
        print(root)

        dirs[:] = [x for x in dirs if not x.startswith('.')]

        for dir in dirs:
            print(os.path.join(root, dir))
        
        files[:] = [x for x in files if not x.startswith('.')]

        for file in files:
            print(os.path.join(root, file))        

# Main
dirreader()

# End