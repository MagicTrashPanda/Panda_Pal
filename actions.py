from character import *

hero = Hero(name="Hero", health=100)
hero.equip(Weapons.iron_sword)
enemy = Enemy(name="Enemy", health=100, weapon=Weapons.short_bow)


async def combat(interaction):
    hero.attack(enemy)
    enemy.attack(hero)
    hero_health_bar = hero.health_bar.draw_update()
    enemy_health_bar = enemy.health_bar.draw_update()
    await interaction.edit_original_response(content=f"{hero.name} dealt {hero.weapon.damage} to "
                                             f"{enemy.name} with {hero.weapon.name}!\n"
                                             f"{enemy.name} dealt {enemy.weapon.damage} to "
                                             f"{hero.name} with {enemy.weapon.name}!\n"
                                             f"{hero_health_bar}\n"
                                             f"{enemy_health_bar}")


