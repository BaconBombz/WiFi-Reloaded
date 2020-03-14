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
def checkAndRunOption(menu, option, optionPairs):
    try: #]-----------------|: Check If User Option Is Number If Not Re-Run mainMenu
        int(option) #]------|
    except ValueError: #]---|
        menu() #]-------|
    else:
        if (int(option) >= 0):           #Check Option Is Number, Check If It Is An Valid Option
            optionPairs[int(option)]()   #Run Coresponding Menu Based Off optionPairs
        else:
            menu()                   #If Not A Valid Option Run Re-Run mainMenu

def exitProgram():
    BBSTDLib.clearScreen()
    sys.exit()

def getInterface():
    print("Please Choose A Wireless Interface:")
    subprocess.run("sudo airmon-ng", shell=True)    #List Interfaces
    BBSTDLib.longLine()
    interface = input("Interface: ")
    return interface

def setInterfaceMonitor():
    BBSTDLib.title("WiFi-Reloaded")
    subprocess.run("sudo airmon-ng start {}".format(interface), shell=True)
    mainMenu()

def setInterfaceManaged():
    BBSTDLib.title("WiFi-Reloaded")
    subprocess.run("sudo airmon-ng stop {}".format(interface), shell=True)
    mainMenu()

#Menus
def mainMenu(option=""):
    optionPairs = {
                    1:changeInterfaceMode,
                    2:monitorWirelessNetworks,
                    0:exitProgram
                  }

    if (option == ""):
        BBSTDLib.title("Wifi-Reloaded")
        print("Current Interface: {}".format(interface))
        BBSTDLib.longLine()

        print("1) Change Interface Mode") #TODO: Add Menu Options
        print("2) Monitor Wireless Networks")
        BBSTDLib.longLine()
        option = input("Option: ")

    checkAndRunOption(mainMenu, option, optionPairs)

def changeInterfaceMode():
    global interface

    optionPairs = {
                    1:setInterfaceMonitor,
                    2:setInterfaceManaged,
                    0:mainMenu
                  }

    BBSTDLib.title("WiFi-Reloaded")
    print("Current Interface: {}".format(interface))
    BBSTDLib.longLine()
    print("1) Set Interface To Monitor Mode")
    print("2) Set Interface To Managed Mode")
    print("0) Go Back To Main Menu")
    BBSTDLib.longLine()
    option = input("[Main Menu/Change Interface Mode] Option: ")

    checkAndRunOption(changeInterfaceMode, option, optionPairs)

def monitorWirelessNetworks():
    print("works")

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
