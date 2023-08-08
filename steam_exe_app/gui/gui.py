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
        
    def select_file(self):
        file_path = filedialog.askopenfilename(
            initialdir=self.initial_directory,
            title="Select a file",
            filetypes=((" files", "*.*"),
                       ("All files", "*.*"))
        )

        if file_path:
            print("Selected file:", file_path)
            self.selected_file = file_path

    def select_multi_files(self):
        file_paths = filedialog.askopenfilenames(
            initialdir=self.initial_directory,
            title="Select multiple files",
            filetypes=(("All files", "*.*"),)
        )

        if file_paths:
            print("Selected files:", file_paths)
            self.selected_multi_files = file_paths


    def select_directory(self, alt_dir=None):
        dir_path = filedialog.askdirectory(initialdir=self.base_directory)
        if dir_path:
            print("Selected Directory:", dir_path)
            self.selected_directory = dir_path

    def run(self):
        self.root.mainloop()

    def close(self):
        self.root.destroy()


class FileSelectionWindow(SelectionWindow):

    def __init__(self, system, initial_directory, base_directory):
        super().__init__(system, initial_directory, base_directory)

        # Message
        file_message = "Please select the executable file or files for the game you would like to have auto-backup"
        self.file_label = tk.Label(self.root, text=file_message, font=("Helvetica", 16), wraplength=300)
        self.file_label.pack(pady=20)

        self.select_button = tk.Button(self.root, text="Select File", command=self.select_file)
        self.select_button.pack(pady=20)

        self.select_multi_button = tk.Button(self.root, text="Select Multiple Files", command=self.select_multi_files)
        self.select_multi_button.pack(pady=20)

    def select_file(self):
        super().select_file()
        # Extended Func for visual message update
        if self.selected_file:
            file_name = [os.path.basename(self.selected_file)]
            file_message = f"Currently Selected File {file_name}"
            self.file_label.config(text=file_message)
            self.file_label.pack(pady=20)

    def select_multi_files(self):
        super().select_multi_files()
        # Extended Func for visual message update
        if self.selected_multi_files:
            file_names = [os.path.basename(path) for path in self.selected_multi_files]
            file_message = f"Currently Selected Files {file_names}"
            self.file_label.config(text=file_message)
            self.file_label.pack(pady=20)

    

class SaveSelectionWindow(SelectionWindow):
    def __init__(self, system, initial_directory, base_directory):
        super().__init__(system, initial_directory, base_directory)

        # Message
        dir_message = "Please select the save location for the game you would like to have auto-backup"
        self.dir_label = tk.Label(self.root, text=dir_message, font=("Helvetica", 16), wraplength=300)
        self.dir_label.pack(pady=20)

        # Create a button to trigger the directory selection
        self.select_button = tk.Button(self.root, text="Select Directory", command=self.select_directory)
        self.select_button.pack(pady=20)
    
    def select_directory(self):
        super().select_directory()
        # Extended Func for visual message update
        if self.selected_directory:

            dir_message = f"Currently Selected Directory: {self.selected_directory}"
            self.dir_label.config(text=dir_message)
            self.dir_label.pack(pady=20)


class CombinedSelectionWindow(SaveSelectionWindow, FileSelectionWindow):
    def __init__(self, system, initial_directory, base_directory, info=None):
        super().__init__(system, initial_directory, base_directory)

        self.info = info
        # self.make_multiple_buttons()

    # def make_multiple_buttons(self):
    #     if self.info:
    #         names = self.info
    #         for name in names:
    #             install_dir = name["install_dir"]
    #             game_name = name["name"]
