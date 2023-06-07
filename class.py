# Class def for qhtml
from curses import *

class Editor:
    def __init__(self,fh=None):
        self.filehand=fh
        self.scr=curses.initstr()
        self.scr.noecho()
        self.scr.cbreak()
