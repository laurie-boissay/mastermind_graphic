#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

# Global import.
import tkinter as tk

# Local import.
from models.save import Save
from models.frame import Frame

"""
In Mastermind you have to find the code.
It was invented by Mordecai Meirowitz.
You have 12 tries.
The number of points depends on the number of tries remaining.
during a test you offer a 4 color code.
The code cannot be made up of blanks.
Normal level : The code cannot contain the same color more than once.
Hard level : The code may contain duplicates.
The game will answer which colors are in the code.
and which colors are in the right places.
colors in the code = (colors in the code - colors in the right place).
"""


s = Save()
s.create_backup_file()

# Used colors.
background_color = "#0C090A"	#Grey

# Window root :
window = tk.Tk()
window.title("Mastermind")
window.attributes("-zoomed", True)# Linux
# self.window.state("zoomed")# Windows
window.config(background=background_color)

f = Frame(window)
f.welcome_settings()

window.mainloop()














"""
cd /home/jaenne/Python/mastermind_graphic
"""
