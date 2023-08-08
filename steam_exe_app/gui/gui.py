import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

class SelectionWindow:

    def __init__(self, system, initial_directory):
        self.root = tk.Tk()
        self.root.title("File Selection")

        self.root.style = tk.ttk.Style()
        self.root.style.theme_use("clam")

        self.window_width = 600
        self.window_height = 400
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_pos = (self.screen_width - self.window_width) // 2
        self.y_pos = (self.screen_height - self.window_height) // 2

        self.root.geometry(f"{self.window_width}x{self.window_height}+{self.x_pos}+{self.y_pos}")
        self.root.minsize(400, 200)

        self.system = system
        self.initial_directory = initial_directory

        self.selected_file = []
        self.selected_directory = []

    def select_file(self):
        '''
        We can add more specificity using self.system if desired.
        However steam/developers are inconsistent with file ext for their games.
        Windows is .exe
        Mac is usually .app but can also be .sh or no file extension
        Linux can be no file extension or .sh
        Current setup allows for a catch all with all files shown.
        '''

        # Select File Path
        file_path = filedialog.askopenfilename(initialdir=self.initial_directory, title="Select a file", filetypes=((" files", "*.*"), ("All files", "*.*")))
        if file_path:
            print("Selected file:", file_path)
            self.selected_file = file_path

    def select_directory(self):
        dir_path = filedialog.askdirectory()
        if dir_path:
            print("Selected Directory:", dir_path)
            self.selected_directory = dir_path

    def run(self):
        self.root.mainloop()

    def close(self):
        self.root.destroy()


class FileSelectionWindow(SelectionWindow):

    def __init__(self, system, initial_directory):
        super().__init__(system, initial_directory)

        # Message
        file_message = "Please select the executable file for the game you would like to have auto-backup"
        self.file_label = tk.Label(self.root, text=file_message, font=("Helvetica", 16), wraplength=300)
        self.file_label.pack(pady=20)

        self.select_button = tk.Button(self.root, text="Select File", command=self.select_file)
        self.select_button.pack(pady=20)

    def select_file(self):
        super().select_file()

        if self.selected_file:
            file_message = f"Currently Selected File {self.selected_file}"
            self.file_label.config(text=file_message)
            self.file_label.pack(pady=20)


class SaveSelectionWindow(SelectionWindow):
    def __init__(self, system, initial_directory):
        super().__init__(system, initial_directory)

        # Message
        dir_message = "Please select the save location for the game you would like to have auto-backup"
        self.dir_label = tk.Label(self.root, text=dir_message, font=("Helvetica", 16), wraplength=300)
        self.dir_label.pack(pady=20)



        # Create a button to trigger the directory selection
        self.select_button = tk.Button(self.root, text="Select Directory", command=self.select_directory)
        self.select_button.pack(pady=20)
    
    def select_directory(self):
        super().select_directory()  # Call the parent class method

        if self.selected_directory:
            dir_message = f"Currently Selected Directory: {self.selected_directory}"
            self.dir_label.config(text=dir_message)
            self.dir_label.pack(pady=20)


class CombinedSelectionWindow(SaveSelectionWindow, FileSelectionWindow):
    def __init__(self, system, initial_directory):
        super().__init__(system, initial_directory)
