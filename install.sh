#!/bin/bash

#Installation Script
read -p "Install WiFi-Reloaded? [yes/no]" installation
if [ $installation == yes ]
then
  clear
  echo "Installing..."
  echo "--------------------------------------------------------------------------------"
  sleep 1
  apt-get update
  echo "--------------------------------------------------------------------------------"
  apt-get install figlet -y
  sleep 1
  echo "--------------------------------------------------------------------------------"
  apt-get install airmon-ng -y
  sleep 1
  echo "--------------------------------------------------------------------------------"
  apt-get install airodump-ng -y
  sleep 1
  echo "--------------------------------------------------------------------------------"
  apt-get install aireplay-ng -y
  sleep 1
  echo "--------------------------------------------------------------------------------"
  apt-get install aircrack-ng -y
  sleep 1
  echo "--------------------------------------------------------------------------------"
  sleep 3
  echo "Setting up Files"
  chmod 777 wifi-reloaded
  mkdir Handshakes
  sleep 1
  echo "--------------------------------------------------------------------------------"
  echo "Adding The Finishing Touches..."
  sleep 1
  echo "--------------------------------------------------------------------------------"
  echo "Done. Execute with ./wifi-reloaded"
  echo "Happy Hacking!"
elif [ $installation == no ]
then
  echo "Alright Then. Good Bye!"
else
  exit
fi
