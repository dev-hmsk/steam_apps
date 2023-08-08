import tkinter as tk
import tkinter.ttk as ttk
import os
from tkinter import filedialog

class SelectionWindow:

    def __init__(self, system, initial_directory, base_directory):
        self.root = tk.Tk()
        self.root.title("File Selection")

        self.root.style = tk.ttk.Style()
        self.root.style.theme_use("clam")

        # Window Dimensions
        self.window_width = 900
        self.window_height = 600
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_pos = (self.screen_width - self.window_width) // 2
        self.y_pos = (self.screen_height - self.window_height) // 2
        self.root.geometry(f"{self.window_width}x{self.window_height}+{self.x_pos}+{self.y_pos}")
        self.root.minsize(400, 200)

        # Init Variables for paths
        self.system = system
        self.initial_directory = initial_directory
        self.base_directory = base_directory

        # Variables for user selected files/dir
        self.selected_file = []  # Single element
        self.selected_multi_files = []  # Multiple elements
        self.selected_directory = []  # Single Element

        # Variable for user selected save location
        self.selected_save_location = []  # Single Element
        
    def select_file(self):  # For single file elements
        file_path = filedialog.askopenfilename(
            initialdir=self.initial_directory,
            title="Select a file",
            filetypes=((" files", "*.*"),
                       ("All files", "*.*"))
        )

        if file_path:
            print("Selected file:", file_path)
            self.selected_file = file_path

    def select_multi_files(self):  # For multiple file elements
        file_paths = filedialog.askopenfilenames(
            initialdir=self.initial_directory,
            title="Select multiple files",
            filetypes=(("All files", "*.*"),)
        )

        if file_paths:
            print("Selected files:", file_paths)
            self.selected_multi_files = file_paths

    def select_directory(self):
        dir_path = filedialog.askdirectory(initialdir=self.base_directory)
        if dir_path:
            print("Selected Directory:", dir_path)
            self.selected_directory = dir_path

    def select_save_location(self):
        dir_path = filedialog.askdirectory(initialdir=self.base_directory)
        if dir_path:
            print("Selected Save Location:", dir_path)
            self.selected_save_location = dir_path

    def run(self):
        self.root.mainloop()

    def close(self):
        self.root.destroy()


class FileSelectionWindow(SelectionWindow):

    def __init__(self, system, initial_directory, base_directory):
        super().__init__(system, initial_directory, base_directory)

        # Message
        file_initial_message = "Please select the executable file/files/directory for the game you would like to have auto-backup"
        self.file_label = tk.Label(self.root, text=file_initial_message, font=("Helvetica", 16), wraplength=300)
        self.file_label.pack(pady=20)

        self.select_button = tk.Button(self.root, text="Select File", command=self.select_file)
        self.select_button.pack(pady=20)

        self.select_multi_button = tk.Button(self.root, text="Select Multiple Files", command=self.select_multi_files)
        self.select_multi_button.pack(pady=20)

        self.select_dir_button = tk.Button(self.root, text="Select Directory", command=self.select_directory)
        self.select_dir_button.pack(pady=20)

    def select_file(self):  # For single file element
        super().select_file()
        # Extended Func for visual message update
        if self.selected_file:
            file_name = [os.path.basename(self.selected_file)]
            file_message = f"Currently Selected File to Save {file_name}"
            self.file_label.config(text=file_message)
            self.file_label.pack(pady=20)

    def select_multi_files(self):  # For multiple file elements
        super().select_multi_files()
        # Extend Func for visual message update
        if self.selected_multi_files:
            file_names = [os.path.basename(path) for path in self.selected_multi_files]
            file_message = f"Currently Selected Files to Save {file_names}"
            self.file_label.config(text=file_message)
            self.file_label.pack(pady=20)

    def select_directory(self):
        super().select_directory()
        # Extend Func for visual message update
        if self.selected_directory:
            dir_name = [os.path.basename(self.selected_directory)]
            dir_message = f"Currently Selected Directory to Save: {dir_name}"
            self.file_label.config(text=dir_message)
            self.file_label.pack(pady=20)


class SaveSelectionWindow(SelectionWindow):
    def __init__(self, system, initial_directory, base_directory):
        super().__init__(system, initial_directory, base_directory)

        # Message
        save_dir_initial_message = "Please select the save location for the files you would like to have auto-backup"
        self.save_dir_label = tk.Label(self.root, text=save_dir_initial_message, font=("Helvetica", 16), wraplength=300)
        self.save_dir_label.pack(pady=20)

        # Create a button to trigger the directory selection
        self.select_button = tk.Button(self.root, text="Select Save Location", command=self.select_save_location)
        self.select_button.pack(pady=20)

    def select_save_location(self):
        super().select_save_location()
        # Extend Func for visual message update
        if self.selected_save_location:
            save_dir_name = [os.path.basename(self.selected_save_location)]
            save_dir_message = f"Currently Selected Directory: {save_dir_name}"
            self.save_dir_label.config(text=save_dir_message)
            self.save_dir_label.pack(pady=20)


class CombinedSelectionWindow(SaveSelectionWindow, FileSelectionWindow):
    def __init__(self, system, initial_directory, base_directory, info=None):
        super().__init__(system, initial_directory, base_directory)

        self.info = info

        # # Create Drop Down Menu
        # self.combobox_label = tk.Label(self.root, text="Select a game:")
        # self.combobox_label.pack(pady=10)
        # self.game_options = [name["name"] for name in info]
        # self.selected_game = tk.StringVar()
        # self.combobox = ttk.Combobox(self.root, textvariable=self.selected_game, values=self.game_options)
        # self.combobox.pack(pady=5)


class ErrorWindow():
    def __init__(self, logger, error_message):
        self.root = tk.Tk()
        self.root.title("Error")

        self.root.style = tk.ttk.Style()
        self.root.style.theme_use("clam")

        # Window Dimensions
        self.window_width = 400
        self.window_height = 200
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_pos = (self.screen_width - self.window_width) // 2
        self.y_pos = (self.screen_height - self.window_height) // 2
        self.root.geometry(f"{self.window_width}x{self.window_height}+{self.x_pos}+{self.y_pos}")
        self.root.minsize(400, 200)

        # Attributes
        self.error_message = error_message

        # Error Message
        self.file_label = tk.Label(self.root, text=self.error_message, font=("Helvetica", 16), wraplength=300)
        self.file_label.pack(pady=20)

    def run(self):
        self.root.mainloop()