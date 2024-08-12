import os
import requests
import logging
import curses
import random
import time

error_color = '\33[1;91m'
success_color = '\033[1;32m'
cod = 54
line = f'{cod}*"_"'

git = 'git pull'
"""
def hacker_animation(stdscr):
    characters = ['0', '1', '#', '*', '%', '$', '@', '!', '^', '&']
    height, width = stdscr.getmaxyx()
    
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    try:
        while True:
            for _ in range(100):
                x = random.randint(0, width - 1)
                y = random.randint(0, height - 1)
                char = random.choice(characters)
                stdscr.addch(y, x, char, curses.color_pair(1))
            
            stdscr.refresh()
            time.sleep(0.05)
    
    except KeyboardInterrupt:
        pass

"""
def Execution():
    try:
        os.system(git)
        import gram1
        print(f"{success_color}Successfully imported gram1 module.")
    except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout) as error:
        print(f"{error_color}There's an exception!!! Error: {error}")
    except ImportError as e:
        print(f"{error_color}Don't edit the module documentation.... or author has not uploaded update yet.\n!!!")
   # curses.wrapper(hacker_animation)

Execution()
