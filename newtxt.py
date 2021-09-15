#! /usr/bin/env python3
# Script Name:      newtxt
# Author:           marburgja
# Last Rev:         2021090114
# Purpose:          create, appends, and deletes a text file

# Libraries
from os import remove

# Main

# Create new .txt, "w" creates file if it doesn't exist
newfile=open('newdoc.txt', 'w')

# Write 3 lines
newfile.write("first line \n")
newfile.write("second line \n")
newfile.write("third line")

# Reads first line of file
newfile=open('newdoc.txt','r')
firstline=newfile.readlines()
print(firstline[0])

# Deletes file
remove("newdoc.txt")

# End