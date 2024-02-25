import json


class Weapon:
    def __init__(self,
                 name: str,
                 weapon_type: str,
                 damage: int,
                 value: int
                 ) -> None:
        self.name = name
        self.weaponType = weapon_type
        self.damage = damage
        self.value = value

    def to_dict(self):
        return {
            'name': self.name,
            'weaponType': self.weaponType,
            'damage': self.damage,
            'value': self.value
        }


class Weapons:
    def __init__(self):
        self.weapon_dict = {}

    def load_weapon_dict(self):

        self.weapon_dict = {}

    def save_to_json(self, filename):
        with open(filename, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.weapon_dict.items()}, f)

    def get_weapon(self, weapon_name):

        return self.weapon_dict[weapon_name]

    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        for k, v in data.items():
            weapon = Weapon(name=v['name'], weapon_type=v['weaponType'], damage=v['damage'], value=v['value'])
            self.weapon_dict[k] = weapon


def create_weapon():
    weapons = Weapons()
    weapons.load_weapon_dict()
    weapons.load_from_json('weapons.json')
    create_name = input("What do you want to name the weapon (Proper capitals and spaces): ")
    create_weapon_type = input("What do you want the type to be (lower case): ")
    create_damage = int(input("What do you want the damage to be: "))
    create_value = int(input("What do you want the value to be: "))
    new_weapon = Weapon(name=create_name,
                        weapon_type=create_weapon_type,
                        damage=create_damage,
                        value=create_value)
    weapons.weapon_dict[create_name] = new_weapon
    weapons.save_to_json('weapons.json')

