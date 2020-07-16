#!/usr/bin/python3.8
# -*-coding:Utf-8 -*


from random import randrange


class Game:
    """
	Attributs and methods necessary to resolve the game.
	"""

    def __init__(self):
        self.allowed = [
            "red", "orange", "yellow", "green", 
            "cyan", "blue", "purple", "pink"
            ]
        self.combination = [9, 9, 9, 9]
        self.code = [8, 8, 8, 8]
        self.tries_counter = 0
        self.good_places = 0
        self.good_colors = 0
        self.mode_choice = "duplicates"
        self.entry = ""

    def set_mode_choice(self, mode):
        self.mode_choice = mode

    def set_self_combination(self, combination):
        self.combination = combination

    def convert_to_color(self, list):
        """
        Each number is converted into a color among those
        authorized.
        Each color is saved in self.combination.
        """
        for i, contenu in enumerate(list):
            # Thank you Linek !
            list[i] = self.allowed[int(contenu)]
   
    def set_genererate_code(self):
        """ 
		The code is a list of four 8.
		Each 8 takes a value between 0 and 7.
		If mode choosed is "not_duplicates" And if there is a double :
			- returns False
		Else :			
			- returns True
		"""        
        for index, element in enumerate(self.code):            
            number = randrange(8)
            self.code[index] = int(number)
            element = number
            if self.mode_choice != "duplicates" and self.code.count(element) > 1:                    
                    return False
        #print("Code : ", self.code)
        return True

    def set_color_comparison(self):
        """ 
		Compares the code and the combination by looking
		for color matches.
		Duplicates the combination in backup_combination;
		For each element in backup_combination :
			For each letter in code:
				if the backup_combination letter has more occurrences  
				than the same letter in the code:
					- Replaces excess occurrences in backup_combination 
					with an "x";
			if letter in backup_combination is in the code :
				- increments self.good_colors by 1.
		Increments the test counter by 1.
		"""
        self.good_colors = 0
        backup_combination = []
        backup_combination.extend(self.combination)
        for i, element in enumerate(backup_combination):
            for index, letter in enumerate(self.code):
                if backup_combination.count(element) > self.code.count(letter):
                    if element == letter:
                        del backup_combination[i]
                        backup_combination.insert(i, "x")
            if backup_combination[i] in self.code:
                self.good_colors += 1
        self.tries_counter += 1

    def set_places_comparison(self):
        """
		Searches for well-placed colors:
		Compares the colors for each similar index of the
		combination list and code list.
		saves the number of well-placed colors in good_places. 
		"""
        self.good_places = 0
        for i, element in enumerate(self.combination):
            for index, letter in enumerate(self.code):
                if i == index:
                    if element == letter:
                        self.good_places += 1        

    def display_result(self):
        """
		Text : displays in 1 line informations necessary 
		for the resolution of the code.
		"""
        
        
        str_1 = str(self.good_colors)
        str_2 = "           "
        
        str_4 = str(self.good_places)        
       
        
        text = (str_1+str_2+str_2+str_4+str_2)
        return text
