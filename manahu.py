import curses
from curses import wrapper

def manahuTerm(stdscr):
    stdscr.clear()
    text1 = "Select A Style"

    h, w = stdscr.getmaxyx()
    x = w // 2 - len(text1)//2 - 20
    y = h//2    - 12

    stdscr.addstr(y, x, text1)


    stdscr.refresh()
    stdscr.getch()

wrapper(manahuTerm)
