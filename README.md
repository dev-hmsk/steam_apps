# steam_apps
Steam Task Manager - collects all .exe files from /common and uses psutil to listen for PIDs of .exe. Converts the Steam provided 
.acf files into list of dicts to create a catalog of game sub directories. Also uses fnmatch to create an exclusionary 
list of directories to reduce computation time. Runs locally without need of Steam API or keys


Currently I am implementing a set of functions that will create a .json of all valid .exe game files from a collection of all the 
.exe files present in the /common directory of Steam. By doing this we can create a dynamic json 
of only game relevant executables while ignoring .exe files like crash handlers, anti cheat software etc.

By filtering through this we will only have to run through the whole common directory once when the user first downloads the repo. 
Every subsequent use will instead read from this now filtered .json instead of having to iterate through the whole directory again. 
I will add functionality to allow the program itself to see if there is a filtered list of .exes before running, as well as give 
the user a choice to "update" his .json file by running the whole proccess again. 

Once this is complete it will be a simple task of utilizing the psutil event listener to look for the specific PID of the user select game. 
On proccess termination the python program will wait a determined time (to allow for the game to fully close and for steam to update its save files)
before copying the save files of the game to a user specified location.
