# basic dependencies
import time
from assets import token, guild_id
# discord.py dependencies
from discord.ext import commands
import discord

# discord bot token & guild ID (server ID)
TOKEN = token
GUILDID = guild_id

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

# initialize CT holder w/ 'None' value
cheesetouch_holder: discord.User = None

# initialize dictionary of users crossing fingers
# FORMAT: discord.User : Timestamp of last time fingers crossed (unix style)
crossed_fingers = dict()

# poke command
# TODO: account for 2 scenarios: pokee has fingers crossed; and pokee not in server
@bot.command(name='poke', aliases=['touch'])
async def await_poke(message, ctx, arg: discord.User):
    # check if message sender is the current cheesetouch holder
    if str(message.author.id) == str(cheesetouch_holder.id):
        # TODO is user in server?
        # TODO if yes, are they crossed?
        cheesetouch_holder = arg
        ctx.send(f"{message.author} passed the cheese-touch to {cheesetouch_holder}!")
    else:
        ctx.send(f"Hey {message.author}! You can't do that! You don't have the cheese touch!")

# whois command
@bot.command(name='whois', aliases=['who is'])
async def await_whois(ctx):
    ctx.send(f"Currently, {cheesetouch_holder} has the cheese touch!")

# TODO cross command
@bot.command(name='cross', aliases=['cross fingers'])
async def await_cross(ctx, message):
    # add author to dictionary of crossed fingers
    crossed_fingers[message.author] = int(time.time())
    # send message
    ctx.send(f"{message.author} has crossed their fingers! They're immune from the cheese touch for 60 seconds!")

# TODO init command

# TODO help command




# run the bot
bot.run(TOKEN.strip())