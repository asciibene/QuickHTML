import tkinter as t
from tkinter import simpledialog

class DualInputDialog_snippets(simpledialog.Dialog):

    def body(self, master):
        t.Label(master, text="Snippet Name:").grid(row=0)
        t.Label(master, text="Inserted Text:").grid(row=1)

        self.e1 = t.Entry(master)
        self.e2 = t.Entry(master)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        return self.e1 # initial focus

    def apply(self):
        s_name_str = self.e1.get()
        s_insert_str = self.e2.get()
        self.result= (s_name_str,s_insert_str)
        super().grab_release()        