import json
from logic.logic import *



# Main 
steamapps_directory = r"C:\Program Files (x86)\Steam\steamapps"
directory = os.path.join(steamapps_directory, "common")

# Load the JSON data from the file
with open ("exclude_files.json") as json_file:
    file_data = json.load(json_file)
with open("exclude_directory.json") as json_dir:
    dir_data = json.load(json_dir)
with open("exclude_exe.json") as json_exe:
    exe_data = json.load(json_exe)

# Access the "exclude_files" & "exclude_directory" list from the loaded data
exclude_files = file_data["exclude_files"]
exclude_directory = dir_data["exclude_directory"]
exclude_exe = exe_data["exclude_exe_words"]

# Filter out non game .exe files and write to a file, this will load again and prevent the need to create it every time



# Find and create list of all remaing .exe files in steamapps/common that are not excluded
unfiltered_exe_files = find_exe_files(directory, exclude_files, exclude_directory)
filtered_exe_files = filter_out_exe_files(unfiltered_exe_files, exclude_exe)

file_path = "filtered_exe.json"
with open(file_path, 'w') as json_filtered_exe:
    json.dump(filtered_exe_files, json_filtered_exe, indent=4)

print(filtered_exe_files)
# Find all pid of games currently running
steam_pid = find_pid_by_file_name("steam.exe")
# games_result = convert_acf_to_game_info(steamapps_directory)
# printout(games_result)
current_pids = current_proccess(steam_pid, filtered_exe_files)

#Target PID (currently Remnant II)
if current_pids:
    target_pid = choose_game_to_backup(current_pids)
else:
    print("No running steam games")
    print("exiting")
    sys.exit(0)

# Register the event listener for process termination and pass the PID to the callback function
psutil.Process(target_pid).wait(lambda proc: on_process_terminated(proc.pid))