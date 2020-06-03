import discord
from discord.ext import commands
from token import token

# discord bot token
TOKEN = token

bot = commands.Bot(command_prefix=('cheesetouch', 'cheese', 'Cheese', 'Cheesetouch', 'ct', 'CT'), case_insensitive=True, help_command=None)

# when bot online
@bot.event
async def on_ready():
    print('Bot online.')
    print(f'Name: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    # set status
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='Cheese Touch'))

# poke command