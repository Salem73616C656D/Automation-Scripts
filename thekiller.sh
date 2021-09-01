#! /bin/bash/

# Script Name:      The Killer
# Author:           marburgja
# Last Rev:         20210730
# Purpose:          View, Select, and Kill a Process

# Functions
listemandkillem(){
    while true
do
    ps aux
    echo "Please Select Your Target:"
    read target
    kill -1 $target
    break
done
}

# Main
echo "Are You Prepared To Kill?"
sleep 3
listemandkillem
sleep 3
echo "Wow...You Actually Killed It"

# End