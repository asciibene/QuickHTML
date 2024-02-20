import tkinter as t
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from custom_dialogs import DualInputDialog_snippets


class App(t.Frame):
    def __init__(self,root, boringhandler=None,master=None):
        super().__init__(master)
        self.root=root
        self.bhandler=boringhandler
        self.scrwidth= root.winfo_screenwidth()               
        self.scrheight= root.winfo_screenheight()
        self.html_elements=[] # This represents the tag elements inside the <body>here</body>              
        # MENUBAR <---<---<----<------<------------------<-----------------------------------<------------
        self.menubar = t.Menu(self)
            # File
        self.file_menu = t.Menu(self.menubar, tearoff=0)#<|
        self.file_menu.add_command(label="New file", command=None)
        self.file_menu.add_command(label="Open file", command=self.menu___open_file)
        self.file_menu.add_command(label="Save as", command=self.menu___save_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit QuickHTML", command=self.quit)
             # Edit
        self.edit_menu = t.Menu(self.menubar, tearoff=0)#<|
        self.edit_menu.add_command(label="Cut", command=None)
        self.edit_menu.add_command(label="Copy", command=None)
        self.edit_menu.add_command(label="Paste", command=None)
        
             # Snippets
        
        self.snip_menu = t.Menu(self.menubar, tearoff=0)#<|
        self.snip_menu.add_separator()
        self.snip_menu.add_command(label="New Snippet", command=self.menu___new_snippets)
             # View 
        self.view_menu = t.Menu(self.menubar, tearoff=0)#<|
        self.view_menu.add_command(label="Hide/Show Snippets list", command=None)
        self.view_menu.add_command(label="Hide/Show Elements list", command=None)
             # Help
        self.help_menu = t.Menu(self.menubar, tearoff=0)#<|
        self.help_menu.add_command(label="About", command=self.menu___about)
             # Add the menus objects to the menubar objects
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.menubar.add_cascade(label="Edit", menu=self.edit_menu)
        self.menubar.add_cascade(label="Snippets", menu=self.snip_menu)
        self.menubar.add_cascade(label="View", menu=self.view_menu)
        self.menubar.add_cascade(label="Help", menu=self.help_menu)

        self.root.config(menu=self.menubar)
        # END MENUBAR <------------------BEGIN SCROLLER ------------------------------
        self.scroller_obj = scrolledtext.ScrolledText(self.root, wrap=t.WORD)
        self.scroller_obj.config(bg='#02020e',fg='white',insertbackground='#35ff46')
        self.scroller_obj.pack(expand=True, fill="both")
        # END SCROLLER <----------------BEGIN STATUSBAR -------------------------------
        self.status_strvar= t.StringVar(value="No file opened....")
        self.status_bar_obj = t.Label(self.root, textvariable=self.status_strvar, bd=1, relief=t.RAISED, anchor=t.W, fg='#68be80')
        # END STATUSBAR <---------------BEGIN SNIP LISTBOX-----------------------------
        self.snipframe=t.Frame(self.scroller_obj)
        self.snipframe.pack(side=t.LEFT, anchor=t.SW)
        self.snippets_strvar = t.StringVar(value=snippets_display_str)
        self.snip_listbox_obj=t.Listbox(self.snipframe, height=8, listvariable=self.snippets_strvar,bg="#000222",selectbackground="#0098b3",selectforeground="#ffcc00")
        ttk.Label(self.snipframe, text="Snippets").pack(side=t.TOP,anchor=t.N,fill=t.X)
        self.snip_listbox_obj.bind('<Double-1>', self.listbox___ins_snip())
        #lbox.bind('<<ListboxSelect>>', func())
        # END SNIP LISTBOX <---------------------------------------------------------------------
        # BEGIN ELEMENTS LISTBOX <------------------BEGIN ELEMENT LISTBOX <------------------BEGIN ELEMENT LISTBOX <------------------BEGIN
        self.elemframe=t.Frame(self.scroller_obj)
        self.elemframe.pack(side=t.RIGHT, anchor=t.SE)
        self.elem_list_strvar = t.StringVar(value=self.html_elements)
        self.elem_listbox_obj = t.Listbox(self.elemframe,height=8,listvariable=self.elem_list_strvar,bg="#000222",selectbackground="#0098b3",selectforeground="#ffcc00")
        ttk.Label(self.elemframe, text="HTML Elements").pack(side=t.TOP,anchor=t.N,fill=t.X)
        # BEGIN BUTTONS <------------------BEGIN BUTTONS <------------------BEGIN BUTTONS <------------------BEGIN
            # Snipet insert <---
        self.snip_ins_butn_obj=t.Button(self.scroller_obj, text="Insert Snippet", command=self.listbox___ins_snip)
        self.snip_ins_butn_obj.pack(side=t.BOTTOM)
        self.update_widgets()

    
    def update_widgets(self):
        self.status_bar_obj.config(textvariable=self.status_strvar)
        self.snip_listbox_obj.config(listvariable=self.snippets_strvar)
        self.elem_listbox_obj.config(listvariable=self.elem_list_strvar)

        self.snipframe.pack(side=t.LEFT, anchor=t.SW)
        self.snip_listbox_obj.pack(side=t.LEFT, anchor=t.W)
        for i in range(0,len(snippets_display_str),2):
            self.snip_listbox_obj.itemconfigure(i, background='#353599')
        self.elem_listbox_obj.pack(side=t.RIGHT, anchor=t.SE)
        self.status_bar_obj.pack(side=t.BOTTOM, fill=t.X)
    def menu___about(self):
        messagebox.showinfo("About QuickHTML", "(c) ASCIIbene \n 2024")


    def listbox___ins_snip(self):
        indexlist=self.snip_listbox_obj.curselection()
        if len(indexlist)==1:
            idx = int(indexlist[0])
            self.scroller_obj.insert(t.INSERT,snippets_insert_str[idx]) #TODO write logic for inserting string of text at cursor position
        else:
            pass    


    def menu___open_file(self):
        open_fileobj=t.filedialog.askopenfile(mode='r')
        if open_fileobj is not None:
            with open(open_fileobj.name, "r") as fh:
                filecontent=fh.read()
                self.scroller_obj.delete(1.0, t.END)
                self.scroller_obj.insert(1.0,filecontent)
                self.status_strvar.set(f"Editing {open_fileobj.name}")
            
    
    def menu___save_as(self):
        saveas_filepath=filedialog.asksaveasfilename()
        scroller_text=self.scroller_obj.get(1.0, t.END)
        if saveas_filepath is not None and scroller_text is not None:
            with open(saveas_filepath, "w+") as fh:
                fh.write(scroller_text)
                #self.scrolled_text.delete(1.0, t.END)
                #self.scrolled_text.insert(1.0, filecontent)
                self.status_strvar.set("Saved file {saveas_filepath}")
                self.update_widgets()
    
    def menu___new_file(self): # TODO
        pass
    

    def menu___new_snippets(self):
        dualinp_obj=DualInputDialog_snippets(self.root)
        r=dualinp_obj.result
        snippets_display_str.append(r[0])
        snippets_insert_str.append(r[1])
        self.bhandler.save_snippets_to_file()
        self.bhandler.load_snippets_from_file() # This is ugly

        self.snippets_strvar.set(snippets_display_str)
        self.status_strvar.set("Saved Snippets.")
        self.update_widgets()
        dualinp_obj.destroy()


    def quit(self) -> None:
        return super().quit()



class BoringTaskHandler:
    SNIP_FILE_PATH="./user_data/snippets.txt"
    def __init__(self):
        pass
    def save_snippets_to_file(self, filepath=SNIP_FILE_PATH) -> bool:
        with open(filepath, "w+") as fh:
            for i in range(len(snippets_display_str)):
                fh.write(f"{snippets_display_str[i]}+:+{snippets_insert_str[i]}"+"\n")
        return True or False

    def load_snippets_from_file(self, filepath=SNIP_FILE_PATH) -> bool:
        with open(filepath, "r") as fh:
            snippets_display_str=[]
            snippets_insert_str=[]
            for line in fh:
                if not len(line.strip()) == 0 :
                    snippets_display_str.append(line.split("+:+")[0])
                    snippets_insert_str.append(line.split("+:+")[1])
                
        return True or False
    

if __name__ == "__main__":
    global snippets_insert_str
    global snippets_display_str
    global boringhandler
    snippets_insert_str=[]
    snippets_display_str=[]

    boringhandler=BoringTaskHandler()
    boringhandler.load_snippets_from_file()
    # GUI STUFF
    root=t.Tk()
    app=App(root,boringhandler)
    root.geometry("%dx%d" % (app.scrwidth, app.scrheight))
    root.title('QuickHTML v0.01')
    app.mainloop()
