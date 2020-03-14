#Program Details
#OS: Linux
#Version 1.0

#Import Global Libraries
import subprocess
import sys

#Import Local Libraries
sys.path.append('lib/')     #Add lib Folder To Runtime For Imports
import BBSTDLib     #Standard Library In All My Programs

#Global Variables
interface = ""

#Functions
def getInterface():
    print("Please Choose A Wireless Interface:")
    subprocess.run("sudo airmon-ng", shell=True)    #List Interfaces
    BBSTDLib.longLine()
    interface = input("Interface: ")
    return interface

#Menus
def mainMenu():
    BBSTDLib.title("Wifi-Reloaded")
    print("Current Interface: {}".format(interface))
    BBSTDLib.longLine()
    print("1) Change Interface Mode") #TODO: Add Menu Options
    print("2) Monitor Wireless Networks")
    BBSTDLib.longLine()
    option = input("Option: ")


def changeInterfaceMode():
    global interface

    BBSTDLib.title("WiFi-Reloaded")
    print("Current Interface: {}".format(interface))
    BBSTDLib.longLine()

#Main
def main():
    global interface
    
    BBSTDLib.checkRoot()

    BBSTDLib.title("Wifi-Reloaded")
    print("By BaconBombz | Version 1.0")
    BBSTDLib.longLine()
    interface = getInterface()

    mainMenu()
    


#Execute Main
main()
