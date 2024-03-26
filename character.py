from weapons import Weapons, Weapon
from health_bar import HealthBar
import json
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.panda_pal
enemies_coll = db.enemies
players_coll = db.players
weapons = Weapons()
weapons.mongo_load()


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
                 user_id: str,
                 weapon: str
                 ) -> None:
        super().__init__(name=name, health=health)
        self.default_weapon = weapons.weapon_dict['Fists']
        self.health_bar = HealthBar(self)
        self.user_id = user_id
        self.weapon = weapons.weapon_dict[weapon]

    def equip(self, weapon) -> None:
        self.weapon = weapon

    def drop(self) -> None:
        self.weapon = self.default_weapon


class Enemy(Character):
    def __init__(self,
                 name: str,
                 health: int,
                 weapon: str
                 ) -> None:
        super().__init__(name=name, health=health)
        self.weapon = weapons.weapon_dict[weapon]
        self.health_bar = HealthBar(self)

    def to_dict(self):
        return {
            'name': self.name,
            'health': self.health,
            'weapon': self.weapon.name
        }


class Players:
    def __init__(self):
        self.player_dict = {}

    def update_db(self):
        for k, v in self.player_dict.items():
            players_coll.update_one({"user_id": k}, {"$set": v.to_dict()})

    def load_


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

    @staticmethod
    def mongo_upload_new(item: dict):
        enemies_coll.insert(item)

    def mongo_load(self):
        for item in enemies_coll.find():
            enemy = Enemy(name=item['name'], health=item['health'], weapon=item['weapon'])
            self.enemy_dict[item['name']] = enemy


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
