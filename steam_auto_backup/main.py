import vdf
import os
import platform
import json

from script.script import *
from gui.gui import *
from logic.logic import *
from logger.logger import *
from model.model import *


def main():

    # Python Script Directory
    # print("Current working directory:", os.getcwd())
    python_script_directory = os.path.dirname(os.path.abspath(__file__))
    # print(python_script_directory)

    # Check OS
    system = platform.system()

    if system == "Linux":  # Execute Linux Code Blocks

        # Get the user's home directory
        user_home = os.path.expanduser("~")

        # Define steamapps & common directory paths
        steamapps_directory = os.path.join(user_home, ".steam", "steam", "steamapps")
        steam_common_directory = os.path.join(steamapps_directory, "common")

        # Define script directory paths
        scripts_dir = os.path.join(user_home, python_script_directory, "script", "linux")
        check_sudo_path = os.path.join(scripts_dir, "check_sudo_privileges.sh")
        initial_setup_path = os.path.join(scripts_dir, "initial_setup.sh")
        steamcmd_path = os.path.join(scripts_dir, "steam_cmd_terminal.sh")

        # Set .vdf/.json paths
        steam_game_info_path = os.path.join(user_home, python_script_directory, "json", "steam_game_info" )

        # Check Sudo priveleges <- Bug
        # sudo_flag = check_sudo_privileges(check_sudo_path)

        # Run initial_setup.sh
        # sh_initial_setup_script(initial_setup_path)

    if system == "Windows": # Execute Windows Code Block
        """
        We need to test this in a Windows OS enviroment. 
        This current code makes assumptions on pathing
        """
        # Get the user's home directory
        user_home = os.environ['USERPROFILE']

        # Define script directory paths
        steamapps_directory = r"C:\Program Files (x86)\Steam\steamapps" 

        # Add in windows specific paths like the Linux above

    """
    Based on above OS-specific path setting the below code should be OS agnostic
    """

    # Check for Steam Directory
    try:
        check_directory(steamapps_directory)

    except MissingDirectoryError as e: # If no Steam Directory exists the program should terminate and log the error code
        error_message = str(e)
        ErrorWindow(error_message)
        CriticalError(e)

    # Create Steam manifest
    games_result = convert_acf_to_game_info(steamapps_directory)
    # printout(games_result)

    # Login in once as Anonymous and then exit to setup SteamCMD CLI
    login_to_steamcmd_as_anon(steamcmd_path, function_name="open_login_quit_steam_cmd")

    # Pass app_id from games_result to create .vdf file with all app info taken from SteamCMD
    list_of_game_info_objs = []
    for game in games_result:
        app_id = game["app_id"]
        get_steamcmd_app_info_script(steamcmd_path, function_name="get_app_info_vdf", app_id=app_id)

        # Convert .vdf files to .json format
        vdf_to_json(steam_game_info_path, app_id)
        # Remove .vdf files <- Not stricly neccisary but makes it cleaner
        remove_vdf_files(steam_game_info_path, app_id)
        # Create game_app_obj
        new_game_info_obj = create_game_app_obj(steam_game_info_path, app_id)
        list_of_game_info_objs.append(new_game_info_obj)

    for obj in list_of_game_info_objs:
        print(obj.name, obj.os_exec_pair)

    # Open Tkinter GUI

    # combined_selection_window = CombinedSelectionWindow(system, steam_common_directory, base_directory, games_result)
    # combined_selection_window.run()

    # # Debug Print
    # print(combined_selection_window.selected_file)
    # print(combined_selection_window.selected_multi_files)
    # print(combined_selection_window.selected_directory)
    # print(combined_selection_window.selected_save_location)

def vdf_to_json(steam_game_info_path, app_id):
    vdf_path = f"{steam_game_info_path}/{app_id}_app_info.vdf"
    json_path = f"{steam_game_info_path}/{app_id}_app_info.json"

    try:
        with open(vdf_path, "r") as file:
            vdf_data = vdf.load(file)
    except FileNotFoundError:
        message = f"Error: VDF file for {app_id} not found."
        logger.error(message)
        return
    except Exception as vdf_load_error:
        message = f"Error: Loading {app_id} VDF:", vdf_load_error
        logger.error(message)
        return
    try:
        json_output = json.dumps(vdf_data, indent=4)
    except Exception as json_dump_error:
        message = f"Error: Converting to {app_id} JSON:", json_dump_error
        logger.error(message)
        return
    try:
        with open(json_path, 'w') as f:
            f.write(json_output)
    except Exception as json_write_error:
        message = f"Error: Writing {app_id} JSON:", json_write_error
        logger.error(message)
        return

    message = f"{app_id} vdf to json Conversion completed successfully."
    logger.info(message)

def remove_vdf_files (steam_game_info_path, app_id):
    if os.path.exists(f"{steam_game_info_path}/{app_id}_app_info.vdf"):
        os.remove(f"{steam_game_info_path}/{app_id}_app_info.vdf")
        message = f"{app_id}_app_info.vdf removed succesfully"
        logger.info(message)
    else:
        message = f"{app_id}_app_info.vdf does not exist"
        print(message)
        logger.error(message)

def create_game_app_obj (steam_game_info_path, app_id):
    if os.path.exists(f"{steam_game_info_path}/{app_id}_app_info.json"):
        with open(f"{steam_game_info_path}/{app_id}_app_info.json", "r") as file:
            data = json.load(file)
            common_name = data.get(app_id, {}).get("common", {}).get("name")
            config_info = data.get(app_id, {}).get("config", {})
            launch_pairings = {}
            for key, value in config_info["launch"].items():
                os_list = value["config"]["oslist"]
                executable = value["executable"]
                launch_pairings[os_list] = executable

            new_game_info_obj = Game_Info(common_name, launch_pairings)
    return new_game_info_obj


if __name__ == "__main__":
    clear_log_files() # clear everything above DEBUG level
    main()






























    # def all_variations_of_game_name(game_list):
    #     new_set = set()
    #     for name in game_list:
    #         check_word_count = name.split()
    #         if len(check_word_count) == 1:
    #             new_set.add(name)
    #         if len(check_word_count) > 1:
    #             capital_letters = [letter for letter in name if letter.isupper()]
    #             numbers = [number for number in name if number.isdigit()]
    #             game_capital_letters = ''.join(capital_letters)
    #             game_numbers = ''.join(numbers)
    #             new_set.add(game_capital_letters+game_numbers)
    #             new_set.add(game_capital_letters)
    #             new_set.add(name.replace(" ", "").replace("\t", "").replace("\n", "").replace("\r", ""))

    #     return new_set

    # # add regex searching to convery possible numerals with numbers
    # final_list_of_possible_game_names = all_variations_of_game_name(game_list)
    # print(final_list_of_possible_game_names)
    # # Find all exe files in \common 
    # unfiltered_exe_files = find_exe_files(steam_common_directory)

    # print(unfiltered_exe_files)

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



