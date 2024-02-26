# Import all necessary classes and asyncio for sleep command
from character import Hero, Enemies
from weapons import Weapons
import asyncio

# create classes for weapons and enemies
weapons = Weapons()
enemies = Enemies()

# load the json files into the classes creating the dictionaries weapon_dict and enemy_dict
enemies.load_from_json('enemies.json')
weapons.load_from_json('weapons.json')


#  This is the combat function that will be called when the user uses the battle command
# It will take the users choices for monster and weapon and then create a hero and enemy
async def combat(interaction, monster_to_fight, weapon_to_equip, user):
    hero = Hero(name=user, health=100)
    hero.equip(weapons.weapon_dict[weapon_to_equip])
    current_enemy = enemies.enemy_dict[monster_to_fight]
    while True:
        await asyncio.sleep(0.25)
        hero.attack(current_enemy)
        current_enemy.attack(hero)
        hero_health_bar = hero.health_bar.draw_update()
        enemy_health_bar = current_enemy.health_bar.draw_update()
        await interaction.edit_original_response(content=f"{hero.name} dealt {hero.weapon.damage} to "
                                                 f"**{current_enemy.name}** with *{hero.weapon.name}*!\n"
                                                 f"**{current_enemy.name}** dealt {current_enemy.weapon.damage} to "
                                                 f"{hero.name} with *{current_enemy.weapon.name}*!\n\n\n"
                                                 f"{hero_health_bar}\n\n"
                                                 f"{enemy_health_bar}")
        if hero.health == 0 or current_enemy.health == 0:
            break

