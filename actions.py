from character import Hero, Enemies
from weapons import Weapons

weapons = Weapons()
enemies = Enemies()

enemies.load_from_json('enemies.json')
weapons.load_from_json('weapons.json')
hero = Hero(name="Hero", health=100)
hero.equip(weapons.weapon_dict['Iron Sword'])


current_enemy = None


async def combat(interaction, monster_to_fight):
    global current_enemy
    current_enemy = enemies.enemy_dict[monster_to_fight]
    hero.attack(current_enemy)
    current_enemy.attack(hero)
    hero_health_bar = hero.health_bar.draw_update()
    enemy_health_bar = current_enemy.health_bar.draw_update()
    await interaction.edit_original_response(content=f"{hero.name} dealt {hero.weapon.damage} to "
                                             f"{current_enemy.name} with {hero.weapon.name}!\n"
                                             f"{current_enemy.name} dealt {current_enemy.weapon.damage} to "
                                             f"{hero.name} with {current_enemy.weapon.name}!\n"
                                             f"{hero_health_bar}\n"
                                             f"{enemy_health_bar}")
    return current_enemy
