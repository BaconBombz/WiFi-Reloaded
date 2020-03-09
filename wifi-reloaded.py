#Program Details

#Import Libraries
import os
import subprocess
import sys

#Global Variables


#Functions
def clearScreen():
    subprocess.run("clear", shell=True)

def getInterface():
    print("Please Choose A Wireless Interface:")
    subprocess.run("sudo airmon-ng", shell=True) #List Interfaces
    longLine()
    interface = input("Interface: ")
    return interface

def longLine():
    columns, rows = os.get_terminal_size(0)
    print(columns * "-")

def title():
    clearScreen()
    subprocess.run("figlet WiFi-Reloaded", shell=True)
    longLine()

#Menus
def mainMenu():
    print("") #TODO: Add Menu Options

#Main
def main():
    if (not os.geteuid()==0): #]-------------------|: Check If Program Has Root Privileges
        sys.exit("Please Run As Root ~ Sudo") #]---|

    title()
    print("By BaconBombz | Version 1.0")
    longLine()
    


#Execute Main
main()
