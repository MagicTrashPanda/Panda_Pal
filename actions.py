from character import Hero, Enemies
from weapons import Weapons
import asyncio

weapons = Weapons()
enemies = Enemies()

enemies.load_from_json('enemies.json')
weapons.load_from_json('weapons.json')

current_enemy = None


async def combat(interaction, monster_to_fight, weapon_to_equip, user, msg_id):
    global current_enemy
    hero = Hero(name=user, health=100)
    hero.equip(weapons.weapon_dict[weapon_to_equip])
    current_enemy = enemies.enemy_dict[monster_to_fight]
    while True:
        await asyncio.sleep(0.25)
        hero.attack(current_enemy)
        current_enemy.attack(hero)
        hero_health_bar = hero.health_bar.draw_update()
        enemy_health_bar = current_enemy.health_bar.draw_update()
        await interaction.followup.edit_message(message_id=msg_id.id,
                                                content=f"{hero.name} dealt {hero.weapon.damage} "
                                                        f"to **{current_enemy.name}** with *{hero.weapon.name}*!\n"
                                                        f"**{current_enemy.name}** dealt {current_enemy.weapon.damage} "
                                                        f"to {hero.name} with *{current_enemy.weapon.name}*!\n\n\n"
                                                        f"{hero_health_bar}\n\n"
                                                        f"{enemy_health_bar}")
        if hero.health == 0 or current_enemy.health == 0:
            break
    return hero, current_enemy
