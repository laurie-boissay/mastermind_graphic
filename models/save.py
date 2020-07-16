#!/usr/bin/python3.8
# -*-coding:Utf-8 -*


import os
import pickle

os.chdir("models")

from models.game import Game


class Save:
    """
	Attributs and methods about the saves file and scores.
	"""

    def __init__(self):
        self.scoreboard = {}
        self.player_score = 0
        self.name = "name"
        
    def set_name(self, name):
        name = name
        if name == "":
            name = "Anonymous"
        self.name = name
        
    def create_backup_file(self):
        """
		This function checks that the "backups" file exists
		if not, it creates the "backup" file with an empty scoreboard.
		"""
        if not os.path.exists("saves"):
            with open("saves", "wb") as file:
                my_pickler = pickle.Pickler(file)
                my_pickler.dump(self.scoreboard)

    def write_backup(self, score):
        """
		Creates a backup on behalf of the player with 0 points.
		"""
        with open("saves", "wb") as file:
            my_pickler = pickle.Pickler(file)
            self.player_score = score
            self.scoreboard[self.name] = self.player_score
            my_pickler.dump(self.scoreboard)
            return self.player_score

    def open_backup(self):
        """
		This methode opens the "backups" file
		then verify that the player has a save in his name.
		if so, it returns the player's score.
		if not, it calls write_backup().
		"""
        with open("saves", "rb") as file:
            my_depickler = pickle.Unpickler(file)
            self.scoreboard = my_depickler.load()
            for player, point in self.scoreboard.items():
                if player == self.name:
                    self.player_score = point
                    return self.player_score
            self.player_score = self.write_backup(0)
            return self.player_score

    def save_score(self, score):
        """
		The function checks if the player's score is higher than his former 
		best score.
		If so, it overwrites the old score and records the new best score.
		if not, it does not touch the backup file.
		"""
        for player, point in self.scoreboard.items():
            # get the player's old score.
            if player == self.name:
                old_score = point                
                # If the player beats her/his old score.
                if old_score < score:
                    self.write_backup(score)

    def compare_score(self):
        """
		Checks if the player's score is higher than his former 
		best score.
		If so, it overwrites the old score and records the new best score.
		if not, it does not touch the backup file.
		"""
        best_score = 0
        for player, point in self.scoreboard.items():
            if point > best_score:
                best_score = point
                best_player = player
        if best_score != 0:
            list = ["The best score is ", str(best_score), " and is owned by :\n"]

            for player, point in self.scoreboard.items():
                if best_score == point:
                    list_2 = ["		-", str(player), "\n"]
                    text = " ".join(list_2)
                    list.append(text)

            if self.player_score == best_score:
                list_3 = [
                    "\nYou have the highest score :",
                    str(best_score),
                    "! Bravo !",
                ]
                text = " ".join(list_3)
                list.append(text)

            text = "".join(list)
            return text
        text = "There are no scores recorded yet."
        return text
