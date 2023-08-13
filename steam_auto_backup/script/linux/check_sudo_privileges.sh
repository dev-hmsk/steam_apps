#!/bin/bash

# Check if sudo privileges are available
if sudo -n true 2>/dev/null; then
    echo "Succes: Sudo privileges are available."
else
    echo "Error: Sudo privileges are not available."
fi
