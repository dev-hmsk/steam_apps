from logic.logic import *


# Main 
directory = r"C:\Program Files (x86)\Steam\steamapps\common"
exclude_files = [""]
exclude_directory = ["C:/Program Files (x86)/Steam/steamapps\common\SteamVRPerformanceTest","C:/Program Files (x86)/Steam/steamapps\common\SteamVR","C:/Program Files (x86)/Steam/steamapps\common\SteamVR"]
exe_files = find_exe_files(directory, exclude_files, exclude_directory)
steam_pid = find_pid_by_file_name("steam.exe")
steamapps_folder = "C:/Program Files (x86)/Steam/steamapps"
games_result = convert_acf_to_game_info(steamapps_folder)
printout(games_result)
current_proccess(steam_pid, exe_files)
