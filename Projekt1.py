import random
class Player():
    def __init__(self, name, difficulty, category = "Newbie", strength = 10, agility = 10, endurance = 10):
        self.name = name
        self.difficulty = difficulty
        self.category = category
        self.strength = strength
        self.agility = agility
        self.endurance = endurance

class Opponent():
    def __init__(self, name, category, strength, agility, endurance):
        self.name = name
        self.category = category
        self.strength = strength
        self.agility = agility
        self.endurance = endurance

def make_save():
    saves[name_of_player] = new_player
saves = {}
current_character = 0
print("Welcome in Boxer Simulator\nPress 'Enter' to continue.")
input()
print(" New Game\n  Load Game\n     Quit")
command = input("Select an option by typing in: 'New game', 'Load game', 'Quit': ")
while command != "Quit":    
    if command == "New game":
        name_of_player = input("What's your name? ")
        if name_of_player in saves.keys():
            name_of_player = input("That name is already taken! Choose a different one: ")
        difficulty_lvl = input("Choose difficulty level:\nEasy\nNormal\nHard\n")
        new_player = Player(name_of_player, difficulty_lvl)
        current_character = new_player
        make_save()
        break
    elif command == ("Load game"):
        for key in saves.keys():
            print(key)
        character_to_load = input("Which character do you want to load back to the ring? ")
        if character_to_load in saves.keys():
            current_character = saves.get(character_to_load,)
        break