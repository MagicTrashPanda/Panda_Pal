# This file contains the Character class and its subclasses, Hero and Enemy.
# It also contains the Enemies class which is used to create and store enemies.
# Import the required classes and json library
from weapons import Weapons, Weapon
from health_bar import HealthBar
import json

# create the weapons class and load the weapons from the weapons.json file
weapons = Weapons()
weapons.load_from_json('weapons.json')


# create the Character class
# This class is the parent class for Hero and Enemy
class Character:
    def __init__(self,
                 name: str,
                 health: int
                 ) -> None:
        self.name = name
        self.health = health
        self.health_max = health

        self.weapon = weapons.weapon_dict['Fists']

# create the attack method for the Character class
    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()


# create the Hero class
class Hero(Character):
    def __init__(self,
                 name: str,
                 health: int,
                 ) -> None:
        super().__init__(name=name, health=health)
        self.default_weapon = weapons.weapon_dict['Fists']
        self.health_bar = HealthBar(self)

# create the equip and drop methods for the Hero class
    def equip(self, weapon) -> None:
        self.weapon = weapon

    def drop(self) -> None:
        self.weapon = self.default_weapon


# create the Enemy class
class Enemy(Character):
    def __init__(self,
                 name: str,
                 health: int,
                 weapon: Weapon
                 ) -> None:
        super().__init__(name=name, health=health)
        self.weapon = weapon
        self.health_bar = HealthBar(self)

# create the to_dict method for the Enemy class
# This method is used to save the enemy to a json file
    def to_dict(self):
        return {
            'name': self.name,
            'health': self.health,
            'weapon': self.weapon.name
        }


# create the Enemies class
# This class is used to create and store enemies
class Enemies:
    def __init__(self):
        self.enemy_dict = {}

    def load_enemy_dict(self):

        self.enemy_dict = {}

# create the save_to_json method for the Enemies class
    def save_to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.enemy_dict.items()}, f)

    def get_enemy(self, enemy_name):

        return self.enemy_dict[enemy_name]

# create the load_from_json method for the Enemies class
# This method takes enemies from a json file and loads them into the enemy_dict as classes
    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        for k, v in data.items():
            enemy = Enemy(name=v['name'], health=v['health'], weapon=weapons.weapon_dict[v['weapon']])
            self.enemy_dict[k] = enemy


# create the create_enemy function to be used in the content creator
def create_enemy():
    weapons.load_from_json('weapons.json')
    enemies = Enemies()
    enemies.load_enemy_dict()
    enemies.load_from_json('enemies.json')
    create_name = input("What would you like to name the monster: ")
    create_health = int(input("How much health should it have: "))
    create_weapon = input("What weapon should it have(must be in weapons.json): ")
    new_enemy = Enemy(create_name,
                      create_health,
                      weapons.weapon_dict[create_weapon])
    enemies.enemy_dict[create_name] = new_enemy
    enemies.save_to_json('enemies.json')
