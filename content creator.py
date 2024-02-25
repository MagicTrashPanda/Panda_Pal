# import necessary files
from character import create_enemy, Enemies
from weapons import create_weapon, Weapons

# assign classes and initialize dictionaries
enemies = Enemies()
weapons = Weapons()
enemies.load_from_json('enemies.json')
weapons.load_from_json('weapons.json')


# Ask what they want to create in a while loop
def creation_tool():
    while True:
        choice = input("What would you like to create: ")
        if choice.lower() in ["enemy", "monster", "creature"]:
            create_enemy()
        elif choice.lower() == "weapon":
            create_weapon()
        elif choice.lower() in ["e", "exit"]:
            break
        else:
            print("that's not an option. If you want to exit type \"exit\"")


creation_tool()
