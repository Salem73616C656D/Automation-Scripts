#! /usr/bin/env python3
# Script Name:      fileseek
# Author:           marburgja
# Last Rev:         20211116
# Purpose:          Search a directory for certain files and print results to screen

# Libraries

import os,time,datetime,hashlib

# Variables

# Functions
def currentime():
    rn=datetime.datetime.now()
    return rn.strftime('%m-%d-%Y %H:%M:%S')

def filesize(patharg):
    size=os.path.getsize(patharg)
    return size
    

def hasher(patharg):
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
        for dir in dirs:
            print(os.path.join(root,dir))
        for file in files:
            print(os.path.join(root,file))
        if name in files:
            pathtofile=os.path.join(root,name)
            fileresult=[currentime(), hasher(pathtofile),filesize(pathtofile) ]
            result[pathtofile]=fileresult
    if result=={}:
        print("Error 404") # printed when there are no results from the scan
    else:
        print("Format: [Time, Hash Value, File Size(Bytes)]")
        print(result) # prints search results
        print("Total Number Found:", len(result)) # prints the number of results from search


# Main

find_all()

# End