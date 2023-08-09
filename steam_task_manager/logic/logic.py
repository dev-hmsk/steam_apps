import os
import re
import sys
import psutil
import json
import fnmatch
import time

def find_pid_by_file_name(file_names):
    if isinstance(file_names, str):
        file_names = {file_names : False}

    pids = {}
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] in file_names:
            pids[process.info['name']] = str(process.info['pid'])
    return pids

def find_exe_files(directory, exclude_files=None, exclude_directories=None):
    exe_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".exe"):
                exe_files.append(file)
        

    #     print(files)
    #     for file in files:
    #         if file.endswith(".exe"):
    #             file_name = os.path.splitext(file)[0] + ".exe"
    #             if exclude_files and any(pattern in file_name for pattern in exclude_files):
    #                 continue
    #             exe_files[file_name] = False

    return exe_files


"""
Make this a list instead of a dict before it gets here, that way its easier to manipulate. 
Right now have the none value doesn't make sense since we can just make it a dict later vs keeping it as a dict and we manipulate it.
"""
# def filter_out_exe_files(unfiltered_exe_files, exclude_exe):
#     filtered_files = []
#     print(unfiltered_exe_files)
#     for file in unfiltered_exe_files:




    # print(exclude_exe)
    # print(unfiltered_exe_files)
    # print(filtered_files)

    # return filtered_files


    # for files in unfiltered_exe_files:
        


def current_proccess(steam_pid, exe_files):
    if steam_pid:
        steam_pid = steam_pid["steam.exe"]
        print(f'Steam is running with the PID of {steam_pid}')
        current_pids = {}
        for game_exe_name in exe_files:
            game_pid = find_pid_by_file_name(game_exe_name)
            if game_exe_name in game_pid:
                print(f'Game "{game_exe_name}" is running with the PID of {game_pid[game_exe_name]}')
                current_pids["game_exe_name"] = game_pid[game_exe_name]
            else:
                print(f'Game "{game_exe_name}" is not running.')
        return current_pids
    else:
        print("Steam is not running.")

def convert_acf_to_game_info(*args):
    steamapps_folder, = args
    manifest_files = [f for f in os.listdir(steamapps_folder) if f.startswith("appmanifest") and f.endswith(".acf")]

    game_info = []
    for manifest_file in manifest_files:
        manifest_path = os.path.join(steamapps_folder, manifest_file)
        with open(manifest_path, "r") as f:
            try:
                manifest_data = f.read()

                app_id = re.search(r'"appid"\s+"(\d+)"', manifest_data)
                game_name = re.search(r'"name"\s+"([^"]+)"', manifest_data)
                install_dir = re.search(r'"installdir"\s+"([^"]+)"', manifest_data)

                if app_id and game_name and install_dir:
                    app_id = app_id.group(1)
                    game_name = game_name.group(1)
                    install_dir = install_dir.group(1)

                    # Get the full path of the install directory
                    install_dir_full_path = os.path.join(steamapps_folder, "common", install_dir)

                    game_info.append({
                        "app_id": app_id,
                        "name": game_name,
                        "install_dir": install_dir_full_path
                    })
                else:
                    print(f"Error processing {manifest_file}: Incomplete data. Skipping this ACF file.")

            except IOError as e:
                print(f"Error reading {manifest_file}: {e}")
    return game_info

def printout(*args):
    print(*args)
    for games_result in args:
        for game in games_result:
            print("App ID:", game["app_id"])
            print("Name:", game["name"])
            print("Install Directory:", game["install_dir"])
            print("-" * 20)

# def log_running_games(*args):
#     running_games = []
#     for process in psutil.process_iter(['name', 'exe']):
#         try:
#             for game in args:
#                 if game in process.info['name']:
#                     running_games.append({
#                         'name': process.info['name'],
#                         'pid': process.pid,
#                         'path': process.info['exe']
#                     })
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             pass

#     if running_games:
#         with open('game_logs.txt', 'w') as f:
#             f.write('Running Games:\n')
#             for game in running_games:
#                 f.write(f"Name: {game['name']}, PID: {game['pid']}, Path: {game['path']}\n")
#             f.write('\n')

def choose_game_to_backup(current_pids):
    print(current_pids)
    print("Type quit to exit program")
    user_input = str(input("Which game do you want to backup?: "))
    if user_input.lower().strip() == 'quit':
        sys.exit(0)
    elif user_input in current_pids:
        print(current_pids[user_input])
        return current_pids[user_input]
    else:
        print("Invalid Choice Try again")
        choose_game_to_backup(current_pids)

def on_process_terminated(pid):
    print(f"The game process with PID {pid} has terminated.")
    # Perform actions or tasks here when the game process stops, e.g., make a copy of the data
