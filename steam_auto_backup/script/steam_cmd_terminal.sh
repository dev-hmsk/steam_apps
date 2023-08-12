#!/bin/bash

# For Steam CMD Terminal
# Navigate to and open Steam CMD

open_steam_cmd () {
    cd ~
    steamcmd
}

# Below are SteamCMD CLI to be used within the CLI from above

# Login in as Anon
login_anonymous () {
    login anonymous
}

#Login in with Steam Account
login_steam_account () {
    echo "Enter your steam username"
    read username
    login $username
}

# Capture and Print result of app_info_print() in the SteamCMD CLI
read appid && echo "$(steamcmd +login anonymous +app_info_print $appid +quit)"

# Capture and Print result of app_info_print() in the SteamCMD CLI with jq for specific info
read appid && echo "$(steamcmd +login anonymous +app_info_print $appid +quit)" > test.txt | 
