import os
import subprocess
from gui.gui import PasswordDialog
from logger.logger import *

def run_shell_script(sh_script_path, new_message=None):
    # Get the sudo password from the user using a GUI dialog
    password_dialog_obj = PasswordDialog()
    if new_message:
        password_dialog_obj.set_message(new_message)

    password = password_dialog_obj.get_password()

    if password is not None:
        try:
            # Run the .sh script using subprocess with sudo
            cmd = ["sudo", "-S", "bash", sh_script_path]
            process = subprocess.Popen(cmd, stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       text=True, bufsize=1)

            # Pass the password directly to the subprocess and get the output
            stdout, stderr = process.communicate(f"{password}\n")
            # logger.info(f"STOUT Terminal Debug: \n {stdout}")

            if "Sorry, try again" in stderr:
                print("Incorrect sudo password entered. Retrying...")
                message = "Incorrect Password Entered. Try Again"
                run_shell_script(sh_script_path, message)  # Recursive message

            elif process.returncode == 0:
                message = "initial_setup.sh script executed successfully."
                print(message)
                logger.info(message)

            else:
                print("Error executing .sh script.")
                print(process.returncode)
                logger.error(stderr)

        except Exception as e:
            logger.error(e)
    else:
        message = "Password not provided. Exiting Program"
        logger.critical(message)
        sys.exit(1)


def run_bat_script(bat_script_path):
    pass


def get_steamcmd_app_info(app_id):
    cmd = ["cd" "~" "steamcmd" ]


def trigger_bash_script(sh_steam_cmd_path, function_name, app_id):
    process = subprocess.Popen([sh_steam_cmd_path, function_name, app_id],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               text=True, bufsize=1)
    
    stdout, stderr = process.communicate()

    print("Standard Output:")
    print(stdout)

    print("Standard Error:")
    print(stderr)
    