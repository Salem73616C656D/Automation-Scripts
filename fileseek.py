#! /usr/bin/env python3
# Script Name:      fileseek
# Author:           marburgja
# Last Rev:         20211116
# Purpose:          Search a directory for certain files and print results to screen

# Libraries
import os
# Variables

# Functions
def find_all():
    path=input("Enter Directory Path To Scan:")
    name=input("Enter Name To Scan For:")
    result=[]
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root,name))
    if result==[]:
        print("Error 404")
    else:
        print(result)
        print("Total Number Found:", len(result))

# Main
find_all()
# End