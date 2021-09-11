#! /usr/bin/env python3
# Script Name:      pylister
# Author:           marburgja
# Last Rev:         202109010
# Purpose:          Assign a variable to list, manipulate list in different ways

# Variables

generic_list = ['thing1', 'thing2', 'thing3', 'thing4', 'thing5', 'thing6', 'thing7', 'thing8', 'thing9', 'thing10']
# Main

# Print 3rd Indexed Item
print(generic_list[3])

# Print Indexed Item 5-10
print(generic_list[5:10])

# Change Indexed Item 7 To A New Item
generic_list[7]= 'newthing'

# Reprint To Veryify Change
print(generic_list)

# End