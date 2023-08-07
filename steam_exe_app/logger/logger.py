import sys
import os
import logging


# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a file handler and set level to debug
file_handler = logging.FileHandler('steam_exe_app/logger/app.log')
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