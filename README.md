# steam_apps
Steam Auto Backup
- Allows the user to select file/files/directory to backup at a specified directory location.
- Use Tkinter for GUI
- Uses .sh and .bat for Linux/Windows setup respectively for SteamCMD installation
- SteamCMD allows users to scan their personal Steam Library for the APPID which will give us all info
- We use this info to find how the developers store their .exe .app etc. files for the game

  Future:
- This info is passed into our process listener. When the app detects the game is running it waits for shutdown to backup
- Some games may allow for backup while running. This is be game-by-game implementation
- Backup can also be set to a timer to update every X minutes/hours/days

Steam Task Manager (currently on hiatus) 
- collects all .exe files from /common and uses psutil to listen for PIDs of .exe.
- Converts the Steam provided .acf files into list of dicts to create a catalog of game sub directories.
- Also uses fnmatch to create an exclusionary list of directories to reduce computation time. Runs locally without need of Steam API or keys

