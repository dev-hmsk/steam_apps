import os
import logging


# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Create the log directory path
log_directory = os.path.join(script_directory, 'logger_info')
os.makedirs(log_directory, exist_ok=True)  # Create the directory if it doesn't exist

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler and set level to debug
log_file_path = os.path.join(log_directory, 'app.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel(logging.DEBUG)

# Create a console handler and set level to debug
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Add formatter to the handlers
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Log messages
# logger.debug("This is a debug message")
logger.info("New Program Execution")

# Exceptions & Function Checks
class MissingDirectoryError(Exception):
    def __init__(self, message):
        super().__init__(message)
        logger.error(message)

def check_directory(directory_name):
    if not os.path.exists(directory_name):
        raise MissingDirectoryError(f"Required {directory_name} is missing!")