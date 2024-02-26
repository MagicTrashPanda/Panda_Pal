# import discord and required files
from settings import *
import discord
from discord import app_commands
from actions import combat

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
async def battle(interaction,
                 monster_to_fight: str,
                 weapon_to_equip: str):
    user = interaction.user.mention
    await interaction.response.send_message("battlefield")
    await combat(interaction, monster_to_fight, weapon_to_equip, user)


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=836717870905163806))
    print(f'We have logged in as {client.user}')

client.run(discordToken)
