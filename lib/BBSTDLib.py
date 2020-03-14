#Import Global Libraries
import os
import subprocess
import sys

#Functions
def checkRoot():
    if (not os.geteuid()==0): #]-------------------|: Check If Program Has Root Privileges
        sys.exit("Please Run As Root ~ Sudo") #]---|

def clearScreen():
    subprocess.run("clear", shell=True)

def longLine():
    columns, rows = os.get_terminal_size(0)
    print(columns * "-")

def title(text):
    clearScreen()
    subprocess.run("figlet {}".format(text), shell=True)
    longLine()