import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog


class FileSelectionWindow:

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

        self.open_button = tk.Button(self.root, text="Select File", command=self.open_file)
        self.open_button.pack(pady=20)


    def open_file(self):
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
            # Do something with the selected file path (e.g., process the file)
            print("Selected file:", file_path)
            self.selected_file = file_path
            self.root.destroy()  # Close the Tkinter window after selection

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    # Example usage of the class
    file_selection_window = FileSelectionWindow("/path/to/directory")
    file_selection_window.run()
