#! /usr/bin/env python3
# Script Name:      wewillrockyou
# Author:           marburgja
# Last Rev:         20211025
# Purpose:          List passwords in wordlist/Search wordlist for input
# Sources:          https://www.geeksforgeeks.org/python-how-to-search-for-a-string-in-text-files/
#                   https://github.com/codefellows/seattle-cyber-401d3/blob/main/class-16/challenges/DEMO.md


# Libraries
import time

# Functions
def main():
    while True:
        choice=input("""
        ***We Will RockYou Menu***
1 - Iterate Dictionary/Wordlist
2 - Search Dictionary/Wordlist
3 - Exit Menu
Please Select Mode:
""")
        if choice=="1":
            iterator()
        elif choice=="2":
            inspector()
            time.sleep(5)
        elif choice=="3":
            break
        else:
            print("Invalid Mode! Try Again.")

def iterator():
    path=input("Enter Path to Wordlist/Dictionary:")
    file=open(path, "r")
    line=file.readline() #reads the lines in the file into variable "line"
    while line:   #reads through the lines of the file and prints them to screen
        line=line.rstrip()
        #word=line   why?
        print(line)
        time.sleep(1)
        line=file.readline()
    file.close()

def inspector():
    path=input("Enter Path to Wordlist/Dictionary:")
    passwd=input("Enter Password For Search:")
    file=open(path, "r")
    flag=0  # sets starting point for the list
    index=0
    for line in file:
        index+=1
        if passwd in line: # if the password matches the current line, break loop
            flag=1
            break

    if flag==1: # if the password was matched above, print confirmation and line number
        print("That Password Was Found!","Line", index)


# Main
main()

# End