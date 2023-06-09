#Quick Html

import curses as curses
import os.path
from helper import *



def main():
  global stdscr,maxsz
  stdscr.clear()
  maxsz[0],maxsz[1] = stdscr.getmaxyx()
  #tofunc! intro screen
  stdscr.addstr(0, 0, "rows {} | cols {}".format(maxsz[0],maxsz[1]))
  stdscr.addstr(maxsz[0]-2, maxsz[1]-3,"X")
  stdscr.nodelay(False)
  k=None
  stdscr.refresh()
  while not k == "q":
      k=stdscr.getkey()
      if k == "l":
          cmd_load_file()
      elif k == "n":
          cmd_new_file()
          return 0
      stdscr.clear()


def cmd_load_file():
  global maxsz, prow, stdscr
  stdscr.clear()
  curses.echo()
  #curses.nocbreak()
  infn=None
  while infn==None or infn == "":
    stdscr.addstr(0,0,"Enter filename to load:")
    stdscr.refresh()
    infn=stdscr.getstr(1,0,15)
    if infn == "^C":
        return 0
    if os.path.exists(infn) is True:
        fn=open(infn, "w")
        stdscr.addstr(2,0,"Loaded file sucessfully, waiting for enterkey....")
        curses.noecho()
        curses.nonl()
        intkey=None
        while not intkey==13:
          intkey=stdscr.getch()
        if intkey==13:
          curses.nl()
          cmd_editor(fn)
    elif os.path.exists(infn) is False:
        stdscr.clear()
        stdscr.addstr(2,0,"File does not exist")
        infn=None
    stdscr.refresh()

def cmd_new_file():
  infn=None
  curses.echo()
  while infn==None or infn == "":
    stdscr.addstr(0,0,"Enter new file name:")
    stdscr.refresh()
    infn=stdscr.getstr(1,0,15)
    fn=open(infn,"w")
  curses.noecho()
  cmd_editor(fn)

######### XXX Main Editor Screen Func XXX ########
def cmd_editor(fh):
  stdscr.clear()
  incmd=None
  flag_exit=False
  while not incmd == "q" or flag_exit is True:
    stdscr.nodelay(False)
    incmd=stdscr.getkey()
    if incmd==":":
      stdscr.move(0,0)
      stdscr.deleteln()
      # ~ stdscr.addstr(0,0,)
    stdscr.addstr(0,0,"Editing file {}".format(fh.name))
    # ~ stdscr.addstr(1,0,scr_drawrow("-"))
    stdscr.refresh()
  fh.close()
  return
####### Editor END ############# Editor END ########    

maxsz=[0,0]

stdscr=curses.initscr()
curses.noecho()
curses.cbreak()
main()
