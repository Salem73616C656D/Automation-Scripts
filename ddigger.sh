#! /bin/bash
# Script Name:      Domain Digger
# Author:           marburgja
# Last Rev:         20210811
# Purpose:          List Info On A Domain

# Functions
domaindigger(){
    whois $domain
    dig $domain
    host $domain
    nslookup $domain
}

# Main
echo "Enter Domain To Query..."
read domain
domaindigger > /home/marburgja/Desktop/domaindigger.txt
gedit /home/marburgja/Desktop/domaindigger.txt

# End