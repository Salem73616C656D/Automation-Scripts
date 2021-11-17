#! /usr/bin/env python3
# Script Name:      fileseek
# Author:           marburgja
# Last Rev:         20211117
# Purpose:          Search a directory for certain files and print results of scan to screen
#                   and give specific details of the file chosen by user

# Libraries

import os,time,datetime,hashlib

# Variables

# Functions
def currentime(): # creates a timestamp to be called 
    rn=datetime.datetime.now()
    return rn.strftime('%m-%d-%Y %H:%M:%S')

def filesize(patharg): # gets filesize of the selected file
    size=os.path.getsize(patharg)
    return size
    
def hasher(patharg): # creates a hash of the selected file
    h=hashlib.md5()
    with open(patharg,'rb') as file:
        chunk=0
        while chunk != b'':
            chunk=file.read(1024)
            h.update(chunk)
    return h.hexdigest()

def find_all():
    path=input("Enter Directory Path To Scan:")
    name=input("Enter Name To Scan For:")
    result={}
    for root, dirs, files in os.walk(path): # searches dirs and sub dirs for "name"
        print(root)
        for dir in dirs: # these for loops print all the directories and files that are being scanned
            print(os.path.join(root,dir))
        for file in files:
            print(os.path.join(root,file))
        if name in files: # if the file is found, add it to the result dictionary
            pathtofile=os.path.join(root,name)
            fileresult=[currentime(), hasher(pathtofile),filesize(pathtofile) ]
            result[pathtofile]=fileresult
    if result=={}:
        print("Error 404") # printed when there are no results from the scan
    else:
        print("""*
*
*
*
*
*
Format: [Time, Hash Value, File Size(Bytes)]
*
*
*
*
*
""")
        print(result) # prints search results
        print("Total Number Found:", len(result)) # prints the number of results from search

# Main

find_all()

# End