#!/bin/bash

# Set DIR locations
BASE_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Check and Upgrade Linux
sudo apt-get update -y 
sudo apt-get update -y 

# Ensure the package system is in a consistent state
sudo dpkg --configure -a || { echo "Failed to configure dpkg. Exiting."; exit 1; }

# Check 32/64 bit system
if [ "$(uname -m)" == "x86_64" ]; then
    # Commands to run if the architecture is x86_64
    echo "You are running a 64-bit system."
    sudo add-apt-repository multiverse -y
    sudo apt install software-properties-common
    sudo dpkg --add-architecture i386
    sudo apt update
    sudo apt install lib32gcc-s1 steamcmd

elif [ "$(uname -m)" == "i686" ] || [ "$(uname -m)" == "i386" ]; then
    echo "You are running a 32-bit system"
fi

# Download SteamCMD
sudo apt install steamcmd



# Clear sudo priveleges at end of script
sudo -k