class Character:
    def __init__(self, name: str,
                 health: int,
                 exp: int,
                 level: int,
                 money: int) -> None:
        self.name = name
        self.health = health
        self.health_max = health
        self.exp = exp
        self.level = level
        self.money = money

    def attack(self, target):
        target.health -= self.weapon_damage
        print(f"{self.name} dealt {self.weapon_damage} to "
              f"{target.name} with {self.weapon.name}")

