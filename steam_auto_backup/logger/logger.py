import os
import sys
import logging
import traceback

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Create the log directory path
log_directory = os.path.join(script_directory, 'logger_info')
os.makedirs(log_directory, exist_ok=True)  # Create the directory if it doesn't exist

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler and set level to DEBUG
log_file_path_debug = os.path.join(log_directory, 'debug.log')
file_handler_debug = logging.FileHandler(log_file_path_debug)
file_handler_debug.setLevel(logging.DEBUG)

# Create a file handler and set level to ERROR
log_file_path_error = os.path.join(log_directory, 'error.log')
file_handler_error = logging.FileHandler(log_file_path_error)
file_handler_error.setLevel(logging.ERROR)

# Create a file handler and set level to CRITICAL
log_file_path_critical= os.path.join(log_directory, 'critical.log')
file_handler_critical = logging.FileHandler(log_file_path_critical)
file_handler_critical.setLevel(logging.CRITICAL)

# Create a console handler and set level to debug
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Add formatter to the handlers
file_handler_debug.setFormatter(formatter)
file_handler_error.setFormatter(formatter)
file_handler_critical.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler_debug)
logger.addHandler(file_handler_error)
logger.addHandler(file_handler_critical)
logger.addHandler(console_handler)

# Log messages
logger.info("New Program Execution")

# Logger Exceptions
class MissingDirectoryError(Exception):
    def __init__(self, message):
        super().__init__(message)
        logger.error(message)


class CriticalError(Exception):
    def __init__(self, e):
        super().__init__()
        logger.critical(f"Critical Error Encountered. Shutting Down Program. {e}")
        sys.exit(1)

# Logger Functions
def check_directory(directory_name):
    if not os.path.exists(directory_name):
        error_message = f"Required {directory_name} is missing!"
        raise MissingDirectoryError(error_message)

def clear_log_files():
    # List of log file names to clear
    log_files = ['error.log', 'critical.log'] # We should always keep debug.log so that there is one .log file with historical data.

    # Clear the contents of each log file
    for log_file in log_files:
        log_file_path = os.path.join(log_directory, log_file)
        with open(log_file_path, 'w') as f:
            f.truncate(0)
