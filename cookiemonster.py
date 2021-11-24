#! /usr/bin/env python3
# Script Name:      fileseek
# Author:           marburgja
# Last Rev:         20211123
# Purpose:          GET cookies

# Libaries
import requests,os,datetime

# Variables
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookies = response.cookies

# Functions
def currentime(): # creates a timestamp to be called 
    rn=datetime.datetime.now()
    return rn.strftime('%m-%d-%Y %H:%M:%S')
  
def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

def yeet_to_sender():
    r=requests.post(targetsite, cookies=cookies)
    return r

def main():
    bringforthcookiemonster()
    #print("Target site is " + targetsite)
    #print(cookies)
    with open("/home/marburgja/Desktop/cookiejar.html", "a") as file:
        file.write(currentime() + ' ' +str(yeet_to_sender()) + "\n")
    os.system("firefox /home/marburgja/Desktop/cookiejar.html")
    exit()
    
# Main
print("""
    __                           __          _      _           
   / /_  __  ___________ ___  __/ /_  ____  (_)    (_)___  _____
  / __ \/ / / / ___/ __ `/ / / / __ \/ __ \/ /    / / __ \/ ___/
 / /_/ / /_/ / /  / /_/ / /_/ / /_/ / /_/ / /    / / / / / /___ 
/_.___/\__,_/_/   \__, /\__, /_.___/\____/_/    /_/_/ /_/\___(_)
                 /____//____/                                   

                                  
      """)
main()

# End