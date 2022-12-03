import prompts.text as txt
import random
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
        self.inventory = dict(Steak = 1, EnergyDrink = 0, ProteinBar = 0)
        self.status = {"Name:": name, "Category:": category, "Strength:": strength, "Agility:": agility, "Endurance:": endurance, "Energy:": self.energy, "Money:": self.money_amount}
        self.location = location
        self.health = strength * 3
        self.battle_stamina = 100
        self.damage_reduction = endurance * 0.75
        
    def throw_straight(self, enemy):
        straight_damage = (straight.base_damage * (self.strength * 0.025)) * ((100 - enemy.damage_reduction) / 100)
        enemy.health -= straight_damage
        self.battle_stamina = straight.endurance_consumption * (self.endurance * 0.0025)
        enemy.battle_stamina -= 10
        print("Your straight deals {}, {} is left with {} hp.".format(straight_damage, enemy.name, enemy.health))
    
    def throw_hook(self, enemy):
        hook_damage = (hook.base_damage * (self.strength * 0.025)) * (enemy.damage_reduction / 100)
        enemy.health -= hook_damage
        self.battle_stamina = hook.endurance_consumption * (self.endurance * 0.0025)
        enemy.battle_stamina -= 20
        print("Your hook deals {}, {} is left with {} hp.".format(hook_damage, enemy.name, enemy.health))
    
    def throw_uppercut(self, enemy):
        uppercut_damage = (uppercut.base_damage * (self.strength * 0.025)) * (enemy.damage_reduction / 100)
        enemy.health -= uppercut_damage
        self.battle_stamina = uppercut.endurance_consumption * (self.endurance * 0.0025)
        enemy.battle_stamina -= 15
        print("Your uppercut deals {}, {} is left with {} hp.".format(uppercut_damage, enemy.name, enemy.health))
    
class SideCharacter():
    def __init__(self, name, category = "Newbie", strength = 10, agility = 10, endurance = 10):
        self.name = name
        self.category = category
        self.strength = strength
        self.agility = agility
        self.endurance = endurance
        self.battle_stamina = 100
        self.health = strength * 3
        self.damage_reduction = endurance * 0.75
        
    def throw_straight(self, enemy):
        straight_damage = (straight.base_damage * (self.strength * 0.025)) * ((100 - enemy.damage_reduction) / 100)
        enemy.health -= straight_damage
        self.battle_stamina = straight.endurance_consumption * (self.endurance * 0.0025)
        enemy.battle_stamina -= 10
        print("Your straight deals {}, {} is left with {} hp.".format(straight_damage, enemy.name, enemy.health))
    
    def throw_hook(self, enemy):
        hook_damage = (hook.base_damage * (self.strength * 0.025)) * (enemy.damage_reduction / 100)
        enemy.health -= hook_damage
        self.battle_stamina = hook.endurance_consumption * (self.endurance * 0.0025)
        enemy.battle_stamina -= 20
        print("Your hook deals {}, {} is left with {} hp.".format(hook_damage, enemy.name, enemy.health))
    
    def throw_uppercut(self, enemy):
        uppercut_damage = (uppercut.base_damage * (self.strength * 0.025)) * (enemy.damage_reduction / 100)
        enemy.health -= uppercut_damage
        self.battle_stamina = uppercut.endurance_consumption * (self.endurance * 0.0025)
        enemy.battle_stamina -= 15
        print("Your uppercut deals {}, {} is left with {} hp.".format(uppercut_damage, enemy.name, enemy.health))
       
class Place():
    def __init__(self, name, is_shop, is_gym, is_home):
        self.name = name
        self.is_shop = is_shop
        self.is_gym = is_gym
        self.is_home = is_home

class Punch():
    def __init__(self, name, base_damage, endurance_consumption):
        self.name = name
        self.base_damage = base_damage
        self.endurance_consumption = endurance_consumption
        
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

def print_formated_text(dict, s,**kwargs):
    print(txt.get_text(dict, s,**kwargs))
    input()

def engage_fight(fighter1, fighter2):
    print("{} VS {}".format(fighter1.name, fighter2.name))
    while fighter1.health > 0 and fighter2.health > 0:
        if fighter1.agility > fighter2.agility:
            print("")
            input()
        else:
            pass
    
locations = dict(
    home = Place("Home", False, False, True),
    gym = Place("Gym", False, True, False),
    shop = Place("Shop", True, False, False) 
)

straight = Punch("straight", 10, 20)
hook = Punch("hook", 20, 30)
uppercut = Punch("uppercut", 15, 25)

bobby = SideCharacter("Bobby", "World Class", 100, 100, 100)
bully1 = SideCharacter("Bully1")

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
            current_character = saves.get(character_to_load)
        break

if command == "New game":
    for text in txt.prompts_intro.keys():
        print_formated_text(txt.prompts_intro, text, bobby=txt.bobby, trainee=txt.trainee, current_character=current_character.name)
    for text in txt.prompts_prolog.keys():
        print_formated_text(txt.prompts_prolog, text, bobby=txt.bobby, current_character=current_character.name)
        
    engage_fight(bobby, bully1)
    
    
print(txt.commands)
while call_command(input()) != "q":
    pass