# steam_apps

## Steam Auto Backup
- Using Tkinter the user chooses which file/files/directory to auto back up in specified locations.
- Creates and listens for game programs to add further functionality and specificy for when to back up save file 
    - (after game close, don't save during game run, save periodically during game run etc.)

### Features
- Automatically detects the operating system and executes the corresponding code block.
    - Linux (complete)
    - Windows (in progress)
    - Mac (future feature)
- Sets up the game directories based on the operating system and initiates an initial setup script (`.sh` or `.bat`).
- Creates a Steam manifest by converting `.acf` files in the Steam directory to game information.
- Utilizes SteamCMD CLI to gather .vdf files of every game in user's common directory and creates .json files for further program use
    - Currently does not require or store Steam Login info, utilizies SteamCMD Anonymous user instead to gather info 
- These .json files allow the program to listen for the relevant executable based on OS (.exe for windows, .app / no extension for Mac/Linux)
- Prompts the user to select game files, directories, and a save location using a GUI interface.
- Performs game backup based on the user's selections.

### Future:
- This info is passed into our process listener. When the app detects the game is running it waits for shutdown to backup
- Some games may allow for backup while running. This is be game-by-game implementation
- Backup can also be set to a timer to update every X minutes/hours/days
- Add Steam User Login and extended functionality due to Steam User privelages (auto update games, activate betas etc.)

## Steam Task Manager (deprecated due to Steam Auto Backup) 
- collects all .exe files from /common and uses psutil to listen for PIDs of .exe.
- Converts the Steam provided .acf files into list of dicts to create a catalog of game sub directories.
- Also uses fnmatch to create an exclusionary list of directories to reduce computation time. Runs locally without need of Steam API or keys

