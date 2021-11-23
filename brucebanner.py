#! /usr/bin/env python3
# Script Name:      Bruce Banner
# Author:           marburgja
# Last Rev:         20211122
# Purpose:          perform banner grabbing via various tools


# Libraries
import os

# Variables

# Function
def destination():
    ipurl=input("Enter Target IP or URL: ")
    return ipurl

def port():
    tgtport=input("Enter Target Port Number: ")
    return tgtport

def netcat():
    query=('nc -N ' +  destination() + ' '+ port())
    print("***Press 'CTL + D' To Exit NETCAT Session***")
    return os.system(query)

def telnet():
    query=('telnet ' +  destination() + ' '+ port())
    print("***Press 'CTL + ]' then 'CTL + D' To Exit TELNET Session***")
    return os.system(query)

def nmap():
    #query=('nmap -sV ' + destination() + ' -p' + port())
    query=('nmap -F ' + destination())
    return os.system(query)

def main():
    while True:
        choice=input("""
        ***Bruce Banner***
1 - Grab Banner With NETCAT
2 - Grab Banner With TELNET
3 - Grab Banner With NMAP
4 - Run All
5 - Exit Menu
Please Select Mode:
""")
        if choice=="1":
            netcat()
            continue
        elif choice=="2":
            telnet()
        elif choice=="3":
            nmap()
        elif choice=="4":
            netcat()
            telnet()
            nmap()
        elif choice=="5":
            break
        else:
            print("Invalid Mode! Try Again.")

# Main
main()

# End
