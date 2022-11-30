import prompts.text as txt

class Player():
    def __init__(self, name, difficulty, location = "Home", category = "Newbie", strength = 10, agility = 10, endurance = 10):
        self.name = name
        self.difficulty = difficulty
        self.category = category
        self.strength = strength
        self.agility = agility
        self.endurance = endurance
        self.energy = 100
        self.money_amount = 50
        self.location = "Home"
        self.inventory = {}
        self.status = {"Name:": name, "Category:": category, "Strength:": strength, "Agility:": agility, "Endurance:": endurance, "Energy:": self.energy, "Money:": self.money_amount}
        self.location = location

class Opponent():
    def __init__(self, name, category, strength, agility, endurance):
        self.name = name
        self.category = category
        self.strength = strength
        self.agility = agility
        self.endurance = endurance   

class Place():
    def __init__(self, name, is_shop, is_gym, is_home):
        self.name = name
        self.is_shop = is_shop
        self.is_gym = is_gym
        self.is_home = is_home

def make_save():
    saves[name_of_player] = new_player

def call_command(command):
    
    if command == "s":
        for key, value in current_character.status.items():
            print(key, value)
       
    elif command == "m":
        print(current_character.location)
        
    elif command == "i":
        for key, value in current_character.inventory.items():
            print(key, value)
    elif command == "q":
        return command

def print_formated_text(s,**kwargs):
    print(txt.get_text(s,**kwargs))
    input()

locations = dict(
    home = Place("Home", False, False, True),
    gym = Place("Gym", False, True, False),
    shop = Place("Shop", True, False, False) 
)

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

if command == "New game":
    for text in txt.prompts.keys():
        print_formated_text(text, bobby=txt.bobby, trainee=txt.trainee, current_character=current_character.name)

print(txt.commands)
while call_command(input()) != "q":
    pass