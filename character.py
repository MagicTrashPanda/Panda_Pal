from weapons import Weapons, Weapon
from health_bar import HealthBar


class Character:
    def __init__(self,
                 name: str,
                 health: int
                 ) -> None:
        self.name = name
        self.health = health
        self.health_max = health

        self.weapon = Weapons.fists

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        # await interaction.followup.send(f"{self.name} dealt {self.weapon.damage} damage to "
        #                                 f"{target.name} with {self.weapon.name}!")


class Hero(Character):
    def __init__(self,
                 name: str,
                 health: int,
                 ) -> None:
        super().__init__(name=name, health=health)
        self.default_weapon = Weapons.fists
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
