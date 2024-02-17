import tkinter as tk
from tkinter import messagebox


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

    def menu_action__about(self):
        tk.messagebox.showinfo("About", "(c)")

    def menu_action__open(self):
        tk.filedialog.askopenfile(mode='r', **options)

    def init_menu(self):
        menubar = tk.Menu(self)
            # File
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="New", command=None)
        file_menu.add_command(label="Open", command=self.menu_action__open)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=file_menu)
            # Edit
        edit_menu = tk.Menu(menubar, tearoff=0)
        edit_menu.add_command(label="Cut", command=None)
        edit_menu.add_command(label="Copy", command=None)
        edit_menu.add_command(label="Paste", command=None)
        menubar.add_cascade(label="Edit", menu=edit_menu)
            # Help
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.menu_action__about)
        menubar.add_cascade(label="Help", menu=help_menu)

if __name__ == "__main__":
    app=App()
    app.init_menu()
