#!/bin/bash

# For Steam CMD Terminal
# Navigate to and open Steam CMD

function open_steam_cmd () {
    cd ~
    steamcmd
}

# Below are SteamCMD CLI to be used within the CLI from above

# Login in as Anon
function login_anonymous () {
    login anonymous
}

#Login in with Steam Account
function login_steam_account () {
    echo "Enter your steam username"
    read username
    login $username
}

# Function to get app info in JSON format
function get_app_info_json () {
    echo "Logging in to SteamCMD..."
    steamcmd +app_info_print "$1" > "${1}_app_info.json" <<EOF
quit
EOF
    sed -n '/Steam>/,$p' "${1}_app_info.json" > temp.json
    mv temp.json "${1}_app_info.json"
    sed -i '1d' "${1}_app_info.json"
}

# Execute the specified function
if [ "$1" == "get_app_info_json" ]; then
    get_app_info_json "$2"
else
    echo "Invalid function name"
fi