#!/usr/bin/python3.8
# -*-coding:Utf-8 -*


"""
Functions what are not useful to resolve the game or to manage the saves file or scores.
"""

def hello_text(name, player_score):
    str_1 = "Hello "
    str_2 = name
    str_3 = " !"
    str_4 = " Your best score is : "
    str_5 = str(player_score)
    text = str_1 + str_2 + str_3 + str_4 + str_5
    return text

def info_text():     
    return """Mastermind was invented by Mordecai Meirowitz.
In Mastermind you have to find the code.
You have 12 tries.
The number of points depends on the number of tries remaining.
During a test you offer a 4 color code.
The code cannot be made up of blanks.
You have to choose if you want duplicates or not in the code.
This game will answer which colors are in the code.
and which colors are in the right places.
Colors in the code = (colors in the code - colors in the right place)."""

def mode_text(mode):
    if mode == "duplicates":
        str_1 = "The code may have duplicates.\n"
    else :
        str_1 = "The code doesn't have duplicates.\n"
    str_2 = "Red pawns are good places, White pawns are bad places."
    text = str_1 + str_2
    return text

def congratz(counter, score):
    str_1 = "Congratulations, you broke the code in "
    str_2 = str(counter) 
    str_3 = " tries.\nYour score is : "
    str_4 = str(score)
    text = str_1 + str_2 + str_3 + str_4
    return text