#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

# Global import.
import tkinter as tk

# Local import.
from models.save import Save
from models.game import Game
from models.texts import *

class Frame:
    def __init__(self, window):
        # Used olors :
        self.background_color = "#0C090A"   #grey
        self.title_color = "#FFEBCD"        #parchment
        self.letter_color = "cyan"     
        self.other_color = "#00FF00"        #green
        self.board_color ="#6F4E37"         #brown
        
        self.window = window
        self.s = Save()
        self.g = Game()
        self.width = 55
        self.height = 55

        self.image_red = tk.PhotoImage(file="red.png").zoom(1).subsample(20)
        self.image_orange = tk.PhotoImage(file="orange.png").zoom(1).subsample(20)
        self.image_yellow = tk.PhotoImage(file="yellow.png").zoom(1).subsample(20)
        self.image_green = tk.PhotoImage(file="green.png").zoom(1).subsample(20)
        self.image_cyan = tk.PhotoImage(file="cyan.png").zoom(1).subsample(20)        
        self.image_blue = tk.PhotoImage(file="blue.png").zoom(1).subsample(20)        
        self.image_purple = tk.PhotoImage(file="purple.png").zoom(1).subsample(20)
        self.image_pink = tk.PhotoImage(file="pink.png").zoom(1).subsample(20)

        self.image_red_pawn_1 = tk.PhotoImage(file="red_pawn_1.png").zoom(1).subsample(20)
        self.image_red_pawn_2 = tk.PhotoImage(file="red_pawn_2.png").zoom(1).subsample(20)
        self.image_red_pawn_3 = tk.PhotoImage(file="red_pawn_3.png").zoom(1).subsample(20)
        self.image_red_pawn_4 = tk.PhotoImage(file="red_pawn_4.png").zoom(1).subsample(20)
        self.image_white_pawn_1 = tk.PhotoImage(file="white_pawn_1.png").zoom(1).subsample(20)
        self.image_white_pawn_2 = tk.PhotoImage(file="white_pawn_2.png").zoom(1).subsample(20)
        self.image_white_pawn_3 = tk.PhotoImage(file="white_pawn_3.png").zoom(1).subsample(20)
        self.image_white_pawn_4 = tk.PhotoImage(file="white_pawn_4.png").zoom(1).subsample(20)
        self.image_no_pawn = tk.PhotoImage(file="no_pawn.png").zoom(1).subsample(20)

        self.combination = {
                            0 : 4,
                            1 : 4,
                            2 : 4,
                            3 : 4
                            }
        self.choice_slot_1 = 0
        self.choice_slot_2 = 0
        self.choice_slot_3 = 0
        self.choice_slot_4 = 0
        
    def my_frame(self):
        """
        Frame :
        """
        self.frame = tk.Frame(
            self.window,
            width=300,
            height=200,
            borderwidth=1,
            bg=self.background_color
        )
        self.frame.pack(fill=tk.BOTH)

    def display_one_line(self, text, size, color):
        """
        Adds a text field of one line.
        """
        self.name_text = tk.Label(
            self.frame, 
            text=text, 
            font=("Arial", size),
            bg=self.background_color, 
            fg=color
        )
        self.name_text.pack(pady=5, side="top", fill=tk.BOTH)

    def display_text(self, text, height):
        """
        Adds a text field of several lines.
        """
        self.info = tk.Text(
            self.frame, 
            height=height,
            width=55,
            font=("Arial", 20),
            bg=self.background_color,
            fg=self.title_color
        )
        self.info.pack(pady=50, side="top")
        self.info.insert(tk.END, text)

    def ask_name(self, size):
        """
        Displays an entry to ask player name.
        """
        self.var_text = tk.StringVar()
        self.name = tk.Entry(
            self.frame, 
            textvariable=self.var_text,
            font=("Arial", size),
            fg=self.letter_color,
            bg=self.title_color, 
            width=20,
        )
        self.name.pack(pady=5, side="top")        
        
    def ask_mode(self):
        """
         Choose your mode :
            - duplicates
            - not duplicates
        """
        self.choice_text = tk.Label(
            self.frame, 
            text="Choose your mode :", 
            font=("Arial", 20),
            bg=self.background_color, 
            fg=self.other_color
        )
        self.choice_text.pack(pady=30, side="top")

        self.mode_choice = tk.StringVar()
        self.duplicates_choice = tk.Radiobutton(
            self.frame,
            text="With duplicates",
            variable=self.mode_choice,
            value="duplicates",
            width=20
        )
        self.duplicates_choice.pack(pady=5, side="top")

        self.no_duplicates_choice = tk.Radiobutton(
            self.frame,
            text="Without duplicates",
            variable=self.mode_choice,
            value="not_duplicates",
            width=20
        )
        self.no_duplicates_choice.pack(pady=5, side="top")

    def add_button(self, text, command, side):
        """        
        Add a button.
        """
        self.new_button = tk.Button(
            self.frame,
            text=text, 
            command=command,
            font=("Arial", 10), 
            bg=self.background_color, 
            fg=self.other_color,
            padx=5,
            pady=5,
            activebackground=self.title_color
        )
        self.new_button.pack(padx=5, pady=30, side=side)
    
    def quit(self):
        """
        Leave the game.
        """
        self.window.destroy()

    def change_settings(self):
        """
        Destroy frame and reload Welcome frame.
        """
        self.frame.destroy()
        self.g.tries_counter = 0
        self.welcome_settings()

    def set_combination_1(self):
        """
        Set combination slot_0.
        """
        self.choice_slot_1 = self.slot_1.curselection()        
        self.choice_slot_1 = self.choice_slot_1[0]
        self.combination[0] = self.choice_slot_1        

    def set_combination_2(self):
        """
        Set combination slot_1.
        """
        self.choice_slot_2 = self.slot_2.curselection()
        self.choice_slot_2 = self.choice_slot_2[0]
        self.combination[1] = self.choice_slot_2        

    def set_combination_3(self):
        """
        Set combination slot_2.
        """
        self.choice_slot_3 = self.slot_3.curselection()
        self.choice_slot_3 = self.choice_slot_3[0]
        self.combination[2] = self.choice_slot_3
        
    def set_combination_4(self):
        """
        Set combination slot_3.
        """
        self.choice_slot_4 = self.slot_4.curselection()
        self.choice_slot_4 = self.choice_slot_4[0]
        self.combination[3] = self.choice_slot_4

# Images___________________________________________________________________
    def display_images_frame(self):
        self.images_frame = tk.Frame(
            self.frame,
            width=self.width,
            height=self.height,
            borderwidth=1,
            bg=self.background_color
        )
        self.images_frame.pack(fill=tk.BOTH)
        self.frame.pack(fill=tk.BOTH)

    def display_image_combinaison(self):
        self.canevas() # Display good colors.
        if self.g.good_colors == 0:            
            self.canvas.create_image(
            self.width/1,
            self.height/2,
            image = self.image_no_pawn
            )
        elif self.g.good_colors == 1:            
            self.canvas.create_image(
            self.width/1,
            self.height/2,
            image = self.image_white_pawn_1
            )
        elif self.g.good_colors == 2:            
            self.canvas.create_image(
            self.width/1,
            self.height/2,
            image = self.image_white_pawn_2
            )
        elif self.g.good_colors == 3:            
            self.canvas.create_image(
            self.width/1,
            self.height/2,
            image = self.image_white_pawn_3
            )
        else: # self.g.good_colors == 4:            
            self.canvas.create_image(
            self.width/1,
            self.height/2,
            image = self.image_white_pawn_4
            )

        self.canvas.pack(side="left", expand=tk.NO)

        for index, color in enumerate(self.g.combination): # Display combination.
            self.canevas()
            self.set_image_combination(self.g.combination[index])

        self.canevas() # Display good places.
        if self.g.good_places == 0:            
            self.canvas.create_image(
            self.width/1,
            self.height/2,
            image = self.image_no_pawn
            )
        elif self.g.good_places == 1:            
            self.canvas.create_image(
            self.width/1,
            self.height/2,
            image = self.image_red_pawn_1
            )

        elif self.g.good_places == 2:            
            self.canvas.create_image(
            self.width/1,
            self.height/2,
            image = self.image_red_pawn_2
            )
        elif self.g.good_places == 3:            
            self.canvas.create_image(
            self.width/1,
            self.height/2,
            image = self.image_red_pawn_3
            )
        else: # self.g.good_colors == 4:            
            self.canvas.create_image(
            self.width/1,
            self.height/2,
            image = self.image_red_pawn_4
            )

        self.canvas.pack(side="left", expand=tk.NO)

    def canevas(self):            
            self.canvas = tk.Canvas(
                self.images_frame, 
                width=self.width*3, 
                height=self.height, 
                bg=self.board_color,
                bd=0,
                highlightthickness=0
                )            

    def set_image_combination(self, color_number):
        if color_number == 0:
            image = self.image_red
        elif color_number == 1:
            image = self.image_orange
        elif color_number == 2:
            image = self.image_yellow
        elif color_number == 3:
            image = self.image_green
        elif color_number == 4:            
            image = self.image_cyan
        elif color_number == 5:
            image = self.image_blue
        elif color_number == 6:
            image = self.image_purple
        else: # color_number == 7
            image = self.image_pink

        self.canvas.create_image(
            self.width/2,
            self.height/2,
            image=image
            )
        self.canvas.pack(side="left", expand=tk.NO)

    def display_image_code(self):
        for index, color in enumerate(self.g.code): # Display combination.
            self.canevas()
            self.set_image_combination(self.g.code[index])

        self.canevas() # Display good places.
    
# Chain of methods_________________________________________________________

    def welcome_settings(self):
        """
        !!! Beginning of the chain !!!

        Welcomes the player.
        Displays info about game.
        Get settings : name and mode choosed.
        Calls confirm button.
        """
        self.g.mode_choice = "duplicates"        
        self.my_frame()
        self.display_one_line("Mastermind", 40, self.letter_color)
        self.display_text(info_text(), 10)
        self.display_one_line("Enter your name :", 20, self.other_color)
        self.ask_name(20)
        self.ask_mode()
        self.add_button("Confirm", self.confirm, "top")
        self.add_button("Quit", self.quit, "bottom")
    
    def confirm(self):
        """
        - Get name and mode ;
        - Save name and mode ;        
        - Call game_progress.
        """        
        self.player_name = self.var_text.get()
        self.mode = self.mode_choice.get()
        if self.mode == "":
            self.mode = self.g.mode_choice
        self.frame.destroy()
        self.s.set_name(self.player_name)
        self.g.set_mode_choice(self.mode)       
        self.game_progress()

    def game_progress(self):
        """
        - Destroy window ;
        - Display name, mode and help about game ;
        - Generate code loop ;
        - Call ask combination.
        """        
        self.g.tries_counter = 0
        self.frame.destroy()
        self.my_frame()
        self.display_one_line(
            hello_text(self.s.name, self.s.open_backup()),# Text.
            20, self.title_color
        )        
        self.display_one_line(
            mode_text(self.g.mode_choice),# Text.
            20, self.title_color
        )
        generate_code = False
        while not generate_code:
            generate_code = self.g.set_genererate_code()
        self.display_one_line("You have 12 tries.", 20, self.other_color)
        #self.display_one_line(help_text(),20, self.other_color)
        self.add_button("Quit", self.quit, "right")
        self.add_button("New part", self.game_progress, "right")
        self.add_button("Settings", self.change_settings, "right")

        self.ask_combination()

    def ask_combination(self):
        # Display 8 color choices for each slot in combination.
        self.slot_1 = tk.Listbox(self.frame)        
        self.slot_1.pack(side="left", pady=5)
        self.confirm_1 = tk.Button(
            self.frame,
            text="Confirm", 
            command=self.set_combination_1,
            font=("Arial", 10), 
            bg=self.background_color, 
            fg=self.other_color,
            padx=5,
            pady=5,
            activebackground=self.title_color
        )
        self.confirm_1.pack(padx=5, pady=30, side="left")

        self.slot_2 = tk.Listbox(self.frame)        
        self.slot_2.pack(side="left", pady=5)
        self.confirm_2 = tk.Button(
            self.frame,
            text="Confirm", 
            command=self.set_combination_2,
            font=("Arial", 10), 
            bg=self.background_color, 
            fg=self.other_color,
            padx=5,
            pady=5,
            activebackground=self.title_color
        )
        self.confirm_2.pack(padx=5, pady=30, side="left")

        self.slot_3 = tk.Listbox(self.frame)        
        self.slot_3.pack(side="left", pady=5)
        self.confirm_3 = tk.Button(
            self.frame,
            text="Confirm", 
            command=self.set_combination_3,
            font=("Arial", 10), 
            bg=self.background_color, 
            fg=self.other_color,
            padx=5,
            pady=5,
            activebackground=self.title_color
        )
        self.confirm_3.pack(padx=5, pady=30, side="left")

        self.slot_4 = tk.Listbox(self.frame)        
        self.slot_4.pack(side="left", pady=5)
        self.confirm_4 = tk.Button(
            self.frame,
            text="Confirm", 
            command=self.set_combination_4,
            font=("Arial", 10), 
            bg=self.background_color, 
            fg=self.other_color,
            padx=5,
            pady=5,
            activebackground=self.title_color
        )
        self.confirm_4.pack(padx=5, pady=30, side="left")

        self.confirm_5 = tk.Button(
            self.frame,
            text="Confirm combination", 
            command=self.comparison,
            font=("Arial", 10), 
            bg=self.background_color, 
            fg=self.other_color,
            padx=5,
            pady=5,
            activebackground=self.title_color
        )
        self.confirm_5.pack(padx=5, pady=30, side="bottom")

        for color in self.g.allowed:# 8 colors.
            self.slot_1.insert(tk.END, color)
            self.slot_2.insert(tk.END, color)
            self.slot_3.insert(tk.END, color)
            self.slot_4.insert(tk.END, color)
        
    def comparison(self):
        """
        Sets the combination in a list ;
        Removes buttons from previous round ;
        Calls :
            - g.set_color_comparison ;
            - g.set_places_comparison ;
            - g.display_result ;
        If game is not over, calls ask_combination ;
        Else, calls end_game.

        """
        self.combination_list = [
            self.combination[0],
            self.combination[1],
            self.combination[2],
            self.combination[3]
            ]        
        self.g.set_self_combination(self.combination_list)

        self.confirm_1.pack_forget()
        self.confirm_2.pack_forget()
        self.confirm_3.pack_forget()
        self.confirm_4.pack_forget()
        self.confirm_5.pack_forget()
        self.slot_1.pack_forget()
        self.slot_2.pack_forget()
        self.slot_3.pack_forget()
        self.slot_4.pack_forget()   
        
        self.g.set_color_comparison()
        self.g.set_places_comparison()
        self.g.good_colors = self.g.good_colors - self.g.good_places
        #print(self.g.display_result())

        self.display_images_frame()
        self.display_image_combinaison()        

        if self.g.good_places < 4 and self.g.tries_counter < 12:            
            self.ask_combination()
        else:           
            self.end_game()

    def end_game(self):
        """
        Set score ;
        If player broke the code calls congratz and save_score ;
        Else calls fail_text ;
        Calls s.compare_score.
        """
        self.frame.destroy()
        self.images_frame.destroy()        
        self.my_frame()

        self.add_button("Quit", self.quit, "right")
        self.add_button("New part", self.game_progress, "right")
        self.add_button("Settings", self.change_settings, "right")
        
        score = (12 - self.g.tries_counter)        
        if self.g.good_places == 4:
            self.display_images_frame()
            self.display_image_code()
            self.display_one_line(
                congratz(self.g.tries_counter, score),#Text.
                20, self.other_color
                )
            self.s.save_score(score)
        else:
            self.display_images_frame()
            self.display_image_code()

            self.display_one_line(
                "You did not break the code.", 
                20, self.other_color)

        self.display_one_line(self.s.compare_score(), 20, self.other_color)
        
       
