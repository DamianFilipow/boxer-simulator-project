import random
class Player():
    def __init__(self, name, difficulty, category = "Newbie", strength = 10, agility = 10, endurance = 10):
        self.name = name
        self.difficulty = difficulty
        self.category = category
        self.strength = strength
        self.agility = agility
        self.endurance = endurance
        self.id = random.randint(1, 100000)

class Opponent():
    def __init__(self, name, category, strength, agility, endurance):
        self.name = name
        self.category = category
        self.strength = strength
        self.agility = agility
        self.endurance = endurance

class SaveFile():
    def __init__(self, name_of_save, character_id):
        self.name_of_save = name_of_save
        self.character_id = character_id

def make_save():
    save = SaveFile(name_of_player, player1.id)
    saves[1] = [save.name_of_save, save.character_id]
saves = {}
main_character_id = 0
print("Welcome in Boxer Simulator\nPress 'Enter' to continue.")
input()
print(" New Game\n  Load Game\n     Quit")
command = input("Select an option by typing in: 'New game', 'Load game', 'Quit': ")
while command != "Quit":    
    if command == "New game":
        name_of_player = input("What's your name? ")
        difficulty_lvl = input("Choose difficulty level:\nEasy\nNormal\nHard\n")
        player1 = Player(name_of_player, difficulty_lvl)
        break
    elif command == ("Load game"):
        pass