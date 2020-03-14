#Program Details
#OS: Linux
#Version 1.0

#Import Global Libraries
import sys

#Import Local Libraries
sys.path.append('lib/')     #Add lib Folder To Runtime For Imports
import BBSTDLib

#Global Variables


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
    print("1) Change Interface Mode") #TODO: Add Menu Options
    print("2) Monitor Wireless Networks")

#Main
def main():
    BBSTDLib.checkRoot()

    BBSTDLib.title("Wifi-Reloaded")
    print("By BaconBombz | Version 1.0")
    BBSTDLib.longLine()
    


#Execute Main
main()
