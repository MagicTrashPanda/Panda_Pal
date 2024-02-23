# import discord and settings
from settings import *
import discord
from discord import app_commands
from character import Hero, Enemy
from weapons import Weapons
from actions import combat, hero, enemy
# declare bot intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# define client and tree for slash commands
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
# hero = Hero(name="Hero", health=100)
# hero.equip(Weapons.iron_sword)
# enemy = Enemy(name="Enemy", health=100, weapon=Weapons.short_bow)
main_interaction = None


# first command
@tree.command(
    name="ping",
    description="My first application Command! It checks latency!",
    guild=discord.Object(id=836717870905163806)
)
async def ping(interaction):
    await interaction.user.send(f'Pong! {round(client.latency * 1000)} ms.')
    await interaction.response.send_message('Sent to your dms!')


# battle command
@tree.command(
    name="battle",
    description="Battle time",
    guild=discord.Object(id=836717870905163806)
)
async def battle(interaction):
    await interaction.response.send_message("battlefield")
    while True:
        await combat(interaction)
        if hero.health == 0 or enemy.health == 0:
            break
    # global main_interaction
    # if main_interaction is None:
    #     await interaction.response.send_message("test")
    #     main_interaction = interaction
    # await main_interaction.edit_original_response(content="test2")


@tree.command(
    name="reset",
    description="reset battle",
    guild=discord.Object(id=836717870905163806)
)
async def reset(interaction):
    hero.health = hero.health_max
    enemy.health = enemy.health_max
    await interaction.response.send_message("battlefield reset have fun!")


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=836717870905163806))
    print(f'We have logged in as {client.user}')

client.run(discordToken)
