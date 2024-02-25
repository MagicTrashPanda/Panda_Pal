# import discord and required files
from settings import *
import discord
from discord import app_commands
from actions import combat, hero, current_enemy

# declare bot intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# define client and tree for slash commands
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


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
async def battle(interaction, monster_to_fight: str = 'Who do you want to fight?'):
    await interaction.response.send_message("battlefield")
    while True:
        enemy = await combat(interaction, monster_to_fight)
        if hero.health == 0 or enemy.health == 0:
            break


@tree.command(
    name="reset",
    description="reset battle",
    guild=discord.Object(id=836717870905163806)
)
async def reset(interaction):
    hero.health = hero.health_max
    current_enemy.health = current_enemy.health_max
    await interaction.response.send_message("battlefield reset have fun!")


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=836717870905163806))
    print(f'We have logged in as {client.user}')

client.run(discordToken)
