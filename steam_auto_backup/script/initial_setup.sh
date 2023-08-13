#!/bin/bash

# Set DIR locations
BASE_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

# Check and Upgrade Linux
sudo apt-get update -y 
sudo apt-get update -y 

# Ensure the package system is in a consistent state
sudo dpkg --configure -a || { echo "Failed to configure dpkg. Exiting."; exit 1; }

# Script Functions
check_distribution() {
    if [ -f "/etc/os-release" ]; then
        source "/etc/os-release"
        if [[ "$ID" == "ubuntu" ]]; then
            echo "Ubuntu distribution detected."
        elif [[ "$ID" == "debian" ]]; then
            echo "Debian distribution detected."
        else
            echo "Unsupported distribution: $ID"
            exit 1
        fi
    else
        echo "Unable to determine distribution."
        exit 1
    fi
}

check_and_install_package() {
    package_name="$1"
    if dpkg -l "$package_name" >/dev/null; then
        echo "$package_name is already installed."
    else
        echo "Installing $package_name..."
        sudo apt-get update
        sudo apt-get install -y "$package_name"
        echo "$package_name installed."
    fi
}

add_architecture_if_missing() {
    target_architecture="$1"
    if ! dpkg --print-foreign-architectures | grep -q "$target_architecture"; then
        echo "Adding $target_architecture architecture..."
        sudo dpkg --add-architecture "$target_architecture"
        sudo apt update
        echo "$target_architecture architecture added."
    else
        echo "$target_architecture architecture already added."
    fi
}

add_repository_if_missing() {
    repository="$1"
    if ! check_repository "$repository"; then
        echo "Adding $repository repository..."
        sudo add-apt-repository "$repository" -y
        sudo apt update
        if check_repository "$repository"; then
            echo "$repository repository added."
        else
            echo "Failed to add $repository repository."
        fi
    else
        echo "$repository repository already added."
    fi
}

check_repository() {
    repository="$1"
    grep -h "^deb .*${repository}" /etc/apt/sources.list /etc/apt/sources.list.d/*
}

# Check Linux Distro
check_distribution

# Check 32/64 bit system
if [ "$(uname -m)" == "x86_64" ]; then
    # Commands to run if the architecture is x86_64
    echo "You are running a 64-bit system."
    # Add multiverse repository
    if [[  "$ID" == "ubuntu"  ]];then
        add_repository_if_missing "multiverse"
    elif [[  "$ID" == "debian"  ]];then
        add_repository_if_missing "deb http://deb.debian.org/debian bullseye main contrib non-free"
        add_repository_if_missing "deb-src http://deb.debian.org/debian bullseye main contrib non-free"
        add_repository_if_missing "deb http://deb.debian.org/debian-security/ bullseye-security main contrib non-free"
        add_repository_if_missing "deb-src http://deb.debian.org/debian-security/ bullseye-security main contrib non-free"
        add_repository_if_missing "deb http://deb.debian.org/debian bullseye-updates main contrib non-free"
        add_repository_if_missing "deb-src http://deb.debian.org/debian bullseye-updates main contrib non-free"
    fi
    check_and_install_package "software-properties-common"
    add_architecture_if_missing "i386"
    check_and_install_package "lib32gcc-s1"

elif [ "$(uname -m)" == "i686" ] || [ "$(uname -m)" == "i386" ]; then
    # Based on SteamCMD readme if the system is 32 bit nothing other than steamcmd needs to be installed.
    # We should test this on 32-bit system to confirm
    echo "You are running a 32-bit system"
fi

# Download SteamCMD
check_and_install_package "steamcmd"

# Run SteamCMD in terminal
<<note
Note: This might need another script to print out the stderr and make it into the tkinter file 
versus keeping in the main setup
note

# cd ~
# steamcmd

# # Login in as anonymous user

# login anonymous

# Clear sudo priveleges at end of script
sudo -k