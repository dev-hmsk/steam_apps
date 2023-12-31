import json
import os
from logic.logic import *

#Program is written to run on Windows OS

#Python Script Directory
print("Current working directory:", os.getcwd())
python_script_directory = os.path.dirname(os.path.abspath(__file__))
print(python_script_directory)

# Steam Directory
steamapps_directory = r"C:\Program Files (x86)\Steam\steamapps"
steam_common_directory = os.path.join(steamapps_directory, "common")

# Create Steam manifest 
games_result = convert_acf_to_game_info(steamapps_directory)
print(games_result)
printout(games_result)

def game_name_list(games_result):
    game_name_list = []
    for game in games_result:
        game_name_list.append(game["name"])
    return game_name_list

game_list = game_name_list(games_result)

print(game_list)

def all_variations_of_game_name(game_list):
    new_set = set()
    for name in game_list:
        check_word_count = name.split()
        if len(check_word_count) == 1:
            new_set.add(name)
        if len(check_word_count) > 1:
            capital_letters = [letter for letter in name if letter.isupper()]
            numbers = [number for number in name if number.isdigit()]
            game_capital_letters = ''.join(capital_letters)
            game_numbers = ''.join(numbers)
            new_set.add(game_capital_letters+game_numbers)
            new_set.add(game_capital_letters)
            new_set.add(name.replace(" ", "").replace("\t", "").replace("\n", "").replace("\r", ""))

    return new_set

# add regex searching to convery possible numerals with numbers
final_list_of_possible_game_names = all_variations_of_game_name(game_list)

# Find all exe files in \common 
unfiltered_exe_files = find_exe_files(steam_common_directory)

print(unfiltered_exe_files)

# # Load the JSON data from the file
# json_file_path = os.path.join(python_script_directory, "json\\")
# with open (json_file_path + "exclude_files.json", "r") as json_file:
#     file_data = json.load(json_file)
# with open(json_file_path + "exclude_directory.json", "r") as json_dir:
#     dir_data = json.load(json_dir)
# with open(json_file_path + "exclude_exe.json", "r") as json_exe:
#     exe_data = json.load(json_exe)

# # Access the "exclude_files" & "exclude_directory" list from the loaded data
# exclude_files = file_data["exclude_files"]
# exclude_directory = dir_data["exclude_directory"]
# exclude_exe = exe_data["exclude_exe_words"]

# # Filter out non game .exe files and write to a file, this will load again and prevent the need to create it every time



# # Find and create list of all remaing .exe files in steamapps/common that are not excluded
# unfiltered_exe_files = find_exe_files(steam_common_directory, exclude_files, exclude_directory)
# # print("hello")
# # print(unfiltered_exe_files)
# # print(exclude_exe)
# filtered_exe_files = filter_out_exe_files(unfiltered_exe_files, exclude_exe)
# print(filtered_exe_files)

# with open(json_file_path + "filtered_exe.json", 'w') as json_filtered_exe:
#     json.dump(filtered_exe_files, json_filtered_exe, indent=4)

# # print(filtered_exe_files)
# # Find steam PID
# steam_pid = find_pid_by_file_name("steam.exe")

# current_pids = current_proccess(steam_pid, filtered_exe_files)


# #Target PID (currently Remnant II)
# if current_pids:
#     target_pid = choose_game_to_backup(current_pids)
# else:
#     print("No running steam games")
#     print("exiting")
#     sys.exit(0)

# # Register the event listener for process termination and pass the PID to the callback function
# psutil.Process(target_pid).wait(lambda proc: on_process_terminated(proc.pid))