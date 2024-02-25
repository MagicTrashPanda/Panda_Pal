from weapons import Weapons, Weapon
from health_bar import HealthBar
import json

weapons = Weapons()
weapons.load_from_json('weapons.json')


class Character:
    def __init__(self,
                 name: str,
                 health: int
                 ) -> None:
        self.name = name
        self.health = health
        self.health_max = health

        self.weapon = weapons.weapon_dict['Fists']

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()


class Hero(Character):
    def __init__(self,
                 name: str,
                 health: int,
                 ) -> None:
        super().__init__(name=name, health=health)
        self.default_weapon = weapons.weapon_dict['Fists']
        self.health_bar = HealthBar(self)

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")

    def drop(self) -> None:
        print(f"{self.name} dropped their {self.weapon}!")
        self.weapon = self.default_weapon


class Enemy(Character):
    def __init__(self,
                 name: str,
                 health: int,
                 weapon: Weapon
                 ) -> None:
        super().__init__(name=name, health=health)
        self.weapon = weapon
        self.health_bar = HealthBar(self)

    def to_dict(self):
        return {
            'name': self.name,
            'health': self.health,
            'weapon': self.weapon.name
        }


class Enemies:
    def __init__(self):
        self.enemy_dict = {}

    def load_enemy_dict(self):

        self.enemy_dict = {}

    def save_to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.enemy_dict.items()}, f)

    def get_enemy(self, enemy_name):

        return self.enemy_dict[enemy_name]

    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        for k, v in data.items():
            enemy = Enemy(name=v['name'], health=v['health'], weapon=weapons.weapon_dict[v['weapon']])
            self.enemy_dict[k] = enemy


def create_enemy():
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
