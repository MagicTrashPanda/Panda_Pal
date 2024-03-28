from pymongo import MongoClient
from character import Enemies, Players
from weapons import Weapons

client = MongoClient("localhost", 27017)
db = client.panda_pal
weapons_coll = db.weapons
enemies_coll = db.enemies


def load_db():
    weapons = Weapons()
    enemies = Enemies()
    players = Players()

    weapons.mongo_load()
    enemies.mongo_load()
    players.mongo_load()
