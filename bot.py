import discord
from discord.ext import commands
from token import token

# discord bot token
TOKEN = token

# init bot
bot = commands.Bot(command_prefix=('cheesetouch', 'cheese', 'Cheese', 'Cheesetouch', 'ct', 'CT'), case_insensitive=True, help_command=None)

# when bot online
@bot.event
async def on_ready():
    print('Bot online.')
    print(f'Name: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    # set status
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='Cheese Touch'))

# TODO init cheese touch holder (random)
cheesetouch_holder_id = ''

# poke command
@bot.command(name='poke', aliases=['touch'])
async def await_poke(message, ctx, arg):
    # check if message sender is the current cheesetouch holder
    if str(message.author.id) == cheesetouch_holder_id:
        arg = arg.replace("<", "")
        arg = arg.replace(">", "")
        arg = arg.replace("@", "")
        cheesetouch_holder_id = str(arg)
        cheesetouch_user = discord.User(id=int(cheesetouch_holder_id))
        ctx.send(f"{message.author} passed the cheese-touch to {cheesetouch_user}!")
    else:
        ctx.send(f"Hey {message.author}! You can't do that! You don't have the cheese touch!")

# whois command
@bot.command(name='whois', aliases=['who is'])
async def await_whois(ctx):
    cheesetouch_user = discord.User(id=int(cheesetouch_holder_id))
    ctx.send(f"Currently, {cheesetouch_user}")

# TODO cross command

# TODO help command