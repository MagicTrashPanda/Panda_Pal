from character import Enemies, Players
from weapons import Weapons
import asyncio

weapons = Weapons()
enemies = Enemies()
players = Players()

weapons.mongo_load()
enemies.mongo_load()
players.mongo_load()


current_enemy = None


async def combat(interaction, monster_to_fight, msg_id, user_id):
    global current_enemy
    hero = players.player_dict[user_id]
    temp_user_id = str(user_id)
    enemies.duplicate_enemy(monster_to_fight, temp_user_id)
    current_enemy = enemies.enemy_dict[monster_to_fight + temp_user_id]
    current_enemy.health = current_enemy.max_health
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
            players.update_player(user_id)
            del enemies.enemy_dict[monster_to_fight + temp_user_id]
            break


async def new_player(user_id, user_name):
    player = players.player_dict.get(user_id)
    if player is None:
        player = players.new_user(user_id, user_name)
    return player


async def heal(user_id):
    player = players.player_dict.get(user_id)
    if player is not None:
        player.health = player.max_health
        player.health_bar.update()
    players.update_player(user_id)
    return player
