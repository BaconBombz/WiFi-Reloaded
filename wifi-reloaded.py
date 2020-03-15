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
def checkAndRunOption(maxOption, menu, option, optionPairs):
    if (option.isdigit()):
        if (int(option) >= 0 and int(option) <= maxOption):     #Check Option Is Number, Check If It Is An Valid Option
            optionPairs[int(option)]()                          #Run Coresponding Menu Based Off optionPairs
        else:
            menu()                                              #If Not A Valid Option Run Re-Run Menu
    else:
        menu()                                                  #If Option Not A Number Re-Run Menu



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

    checkAndRunOption(2, changeInterfaceMode, option, optionPairs)



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
        print("0) Exit")
        BBSTDLib.longLine()
        option = input("Option: ")

    checkAndRunOption(2, mainMenu, option, optionPairs)



def monitorWirelessNetworks():
    BBSTDLib.title("WiFi-Reloaded")
    print("Current Interface: {}".format(interface))
    BBSTDLib.longLine()
    print("Opening Second Window...")
    subprocess.run("sudo xterm -hold -e 'echo Press Ctrl-C To Stop; sudo airodump-ng start {}'".format(interface), shell=True)




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
