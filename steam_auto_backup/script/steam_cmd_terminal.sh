#!/bin/bash

# Set DIR locations
BASE_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
SAVE_DIR="$BASE_DIR/../json/steam_game_info"

# Navigate to and open Steam CMD
function open_steam_cmd () {
    cd ~
    steamcmd
}

# Login in as Anon
function login_anonymous () {
    login anonymous
}

# Quit SteamCMD
function quit_steam_cmd () {
    quit
}

# This function is for the initial app start to have the SteamCMD CLI 
# recognize that future commands will come from the anonymous user group
# versus a steam_id login and password.

function open_login_quit_steam_cmd() {
    echo "Navigating to and opening Steam CMD..."
    cd ~
    steamcmd +login anonymous << EOF
quit
EOF
}

#Login in with Steam Account
function login_steam_account () {
    echo "Enter your steam username"
    read username
    login $username
}

# Function to get app info in JSON format
function get_app_info_json () {
    echo "Creating ${1}_app_info.json"
    steamcmd +app_info_print "$1" > "$SAVE_DIR/${1}_app_info.json" <<EOF
quit
EOF
    echo "Saving ${1}_app_info.json in $SAVE_DIR"
    sed -n '/Steam>/,$p' "$SAVE_DIR/${1}_app_info.json" > "$SAVE_DIR/temp.json"
    mv "$SAVE_DIR/temp.json" "$SAVE_DIR/${1}_app_info.json"
    
    echo "Cleaning up ${1}_app_info.json by removing non-json elements"
    sed -i '1d' "$SAVE_DIR/${1}_app_info.json"
}

# Execute the specified function
if [ "$1" == "get_app_info_json" ]; then
    echo "Executing get_app_info_json with $2"
    get_app_info_json "$2"
elif [ "$1" == "open_login_quit_steam_cmd" ]; then
    echo "Executing open_login_quit_steam_cmd"
    open_login_quit_steam_cmd
else
    echo "Invalid function name"
fi