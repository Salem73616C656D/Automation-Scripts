#! /bin/bash
# Script Name:      ipmenu
# Author:           marburgja
# Last Rev:         20210902
# Purpose:          creates menu for various ip commands
# Reference:        https://askubuntu.com/questions/1705/how-can-i-create-a-select-menu-in-a-shell-script

# Variables
list=("Hello World" "Ping Self" "IP Info" "Exit")
# Functions

# Main
echo "Please Choose An Option:"
select choice in "${list[@]}"
do 
    case $choice in
        "Hello World")
            echo "Hello World"
            ;;
        "Ping Self")
            ping -c 4 127.0.0.1
            ;;
        "IP Info")
            ip a
            ;;
        "Exit")
            break
            ;;
    esac
done

# End