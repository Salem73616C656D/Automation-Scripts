#! /env/bin/python3
# Script Name:          psutil
# Author:               marburgja
# Last Rev:             20210915
# Purpose:              use psutil to give various processes
# Reference:            Courtney Hans (thank you)

# Commands
# sudo apt install python3
# sudo apt install python3-pip
# sudo pip install psutil


# Libraries
import psutil

# Variables
userNormal = repr(psutil.cpu_times().user)
kernelNormal = repr(psutil.cpu_times().system)
idle = repr(psutil.cpu_times().idle)
userPriority = repr(psutil.cpu_times().nice)
completeIO = repr(psutil.cpu_times().iowait)
hardInterupt = repr(psutil.cpu_times().irq)
softInterupt = repr(psutil.cpu_times().softirq)
virtualOS = repr(psutil.cpu_times().steal)
virtualCPU = repr(psutil.cpu_times().guest)


# Main
print("Time spent by normal processes executing in user mode:",userNormal,"seconds")
print("Time spent by normal processes executing in kernel mode:",kernelNormal,"seconds")
print("Time when system was idle:",idle,"seconds")
print("Time spent by priority processes executing in user mode:",userPriority,"seconds")
print("Time spent waiting for I/O to complete:",completeIO,"seconds")
print("Time spent for servicing hardware interrupts:",hardInterupt,"seconds")
print("Time spent for servicing software interrupts:",softInterupt,"seconds")
print("Time spent by other operating systems running in a virtualized environment:",virtualOS,"seconds")
print("Time spent running a virtual CPU for guest OS under the control of the Linux kernal:",virtualCPU,"seconds")

myFile = open("psutilOuput.txt", "w+")
myFile.write("Time when system was idle: " + userNormal +" seconds \n")
myFile.write("Time spent by normal processes executing in kernel mode: " + kernelNormal+" seconds \n")
myFile.write("Time when system was idle: " + idle +" seconds \n")
myFile.write("Time spent by priority processes executing in user mode: " + userPriority +" seconds \n")
myFile.write("Time spent waiting for I/O to complete: " + completeIO +" seconds \n")
myFile.write("Time spent for servicing hardware interrupts: " + hardInterupt +" seconds \n")
myFile.write("Time spent for servicing software interrupts: " + softInterupt +" seconds \n")
myFile.write("Time spent by other operating systems running in a virtualized environment: " + virtualOS +" seconds \n")
myFile.write("Time spent running a virtual CPU for guest OS under the control of the Linux kernal: " + virtualCPU +" seconds")
myFile.close()