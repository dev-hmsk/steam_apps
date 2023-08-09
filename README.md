# steam_apps

## Steam Auto Backup
- Using Tkinter the user chooses which file/files/directory to auto back up in specified locations.

### Features
- Automatically detects the operating system (Linux or Windows) and executes the corresponding code block.
- Sets up the game directories based on the operating system and initiates an initial setup script (`.sh` or `.bat`).
- Creates a Steam manifest by converting `.acf` files in the Steam directory to game information.
- Prompts the user to select game files, directories, and a save location using a GUI interface.
- Performs game backup based on the user's selections.

### Future:
- This info is passed into our process listener. When the app detects the game is running it waits for shutdown to backup
- Some games may allow for backup while running. This is be game-by-game implementation
- Backup can also be set to a timer to update every X minutes/hours/days

## Steam Task Manager (currently on hiatus) 
- collects all .exe files from /common and uses psutil to listen for PIDs of .exe.
- Converts the Steam provided .acf files into list of dicts to create a catalog of game sub directories.
- Also uses fnmatch to create an exclusionary list of directories to reduce computation time. Runs locally without need of Steam API or keys

