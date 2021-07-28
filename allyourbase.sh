# Script Name:      Login Activity Puller
# Author:           marburgja
# Last Rev:         20210728
# Purpose:          List Login Activity

#! /bin/bash/

# Variables
listem=$(last)

# Functions
allyourbase(){
    echo $listem
    echo $listem >> allyourbase.txt
}

# Main

allyourbase

# End