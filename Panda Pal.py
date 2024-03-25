# import discord and required files
from settings import discordToken
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


class CombatMonsterDropdown(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label='Goblin',
                                 description='Fight a Goblin 👹',
                                 value='Goblin'),
            discord.SelectOption(label='Spider',
                                 description='Fight a Spider 🕷️',
                                 value='Spider'),
            discord.SelectOption(label='Mountain Lion',
                                 description='Fight a Mountain Lion 🦁',
                                 value='Mountain Lion'),
        ]
        super().__init__(placeholder='Choose a monster to fight',
                         options=options,
                         min_values=1,
                         max_values=1)

    async def callback(self, interaction):
        self.view.stop()
        # await interaction.edit_original_response(content='You chose {self.values[0]}', view=None)


class BattleView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(CombatMonsterDropdown())


# battle command
@tree.command(
    name="battle",
    description="Battle time",
    guild=discord.Object(id=836717870905163806)  # This is the ID for my test discord
)
# This is the code for our battle command
# we use mandatory arguments to get the users choices for combat then import them into the combat function
async def battle(interaction,
                 weapon_to_equip: str):
    user = interaction.user.mention
    view = BattleView()
    await interaction.response.send_message("Choose a Monster to fight", view=view)
    await view.wait()  # wait for the user to make a selection
    monster_to_fight = view.children[0].values[0]  # get the value of the selection
    await interaction.delete_original_response()
    msg_id = await interaction.followup.send("battle field")
    await combat(interaction, monster_to_fight, weapon_to_equip, user, msg_id)


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=836717870905163806))
    print(f'We have logged in as {client.user}')

client.run(discordToken)
