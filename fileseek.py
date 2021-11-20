#! /usr/bin/env python3
# Script Name:      fileseek
# Author:           marburgja
# Last Rev:         20211117
# Purpose:          Search a directory for certain files and print results of scan to screen
#                   and give specific details of the file chosen by user

# Libraries

import os,datetime,hashlib,time
from dotenv import load_dotenv

# Variables

# Functions
def currentime(): # creates a timestamp to be called 
    rn=datetime.datetime.now()
    return rn.strftime('%m-%d-%Y %H:%M:%S')

def virusscan(pathtofile):
    load_dotenv()
    apikey=os.environ.get("API_KEY") # Set your environment variable before proceeding. You'll need a free API key from virustotal.com so get signed up there first.
    # This concatenates everything into a working shell statement that gets passed into virustotal-search.py
    query=('python3 virustotal-search.py -k ' + str(apikey) + ' -m ' + hasher(pathtofile))
    scan=os.system(query)
    return scan#os.system(query)

def filesize(pathtofile): # gets filesize of the selected file
    size=os.path.getsize(pathtofile)
    return size
    
def hasher(pathtofile): # creates a hash of the selected file
    h=hashlib.md5()
    with open(pathtofile,'rb') as file:
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
        #print(root)
        #for dir in dirs: # these for loops print all the directories and files that are being scanned
        #    print(os.path.join(root,dir))
        #for file in files:
        #    print(os.path.join(root,file))
        if name in files: # if the file is found, add it to the result dictionary
            pathtofile=os.path.join(root,name)
            #hash=hasher(pathtofile)
            fileresult=[currentime(), hasher(pathtofile),filesize(pathtofile),virusscan(pathtofile)]
            #virusscan(pathtofile)
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
        print("Total Number Scanned:", len(files)) # prints the number of files scanned
# Main

find_all()

# End