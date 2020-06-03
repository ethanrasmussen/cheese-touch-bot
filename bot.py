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
guild: discord.Guild

# when bot online
@bot.event
async def on_ready():
    # console output
    print('Bot online.')
    print(f'Name: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    # join guild/server
    guild = bot.get_guild(GUILDID)
    # set status
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='Cheese Touch'))

# initialize CT holder w/ 'None' value
cheesetouch_holder: discord.User = None

# initialize dictionary of users crossing fingers
# FORMAT: discord.User : Timestamp of last time fingers crossed (unix style)
crossed_fingers = dict()

# poke command
# accounts for 2 scenarios: pokee has fingers crossed; and pokee not in server
@bot.command(name='poke', aliases=['touch'])
async def await_poke(message, ctx, arg: discord.User):
    # check if message sender is the current cheesetouch holder
    if message.author.id == cheesetouch_holder.id:
        # is user in server?
        if guild.get_member(arg.id) is not None:
            # if yes, do they have their fingers crossed?
            finger_timestamp = crossed_fingers.get(arg)
            # if time since fingers crossed is 60s or less, they're safe
            if int(time.time()) - finger_timestamp <= 60:
                ctx.send(f"Nice try! But {arg} still has their fingers crossed!")
            # else, they're the new cheesetouch holder!
            else:
                cheesetouch_holder = arg
                ctx.send(f"{message.author} passed the cheese-touch to {cheesetouch_holder}!")
        else:
            ctx.send(f"Hey! You can't give the cheese touch to somebody not on the server!")
    else:
        ctx.send(f"Hey {message.author}! You can't do that! You don't have the cheese touch!")

# whois command
@bot.command(name='whois', aliases=['who is'])
async def await_whois(ctx):
    ctx.send(f"Currently, {cheesetouch_holder} has the cheese touch!")

# cross command
@bot.command(name='cross', aliases=['cross fingers'])
async def await_cross(ctx, message):
    # if user is the cheese touch holder, mock them
    if guild.get_member(message.author.id) == cheesetouch_holder.id:
        ctx.send(f"Really {message.author}? Nice try... but you already have the cheese touch!")
    # else, cross their fingers
    else:
        # add author to dictionary of crossed fingers
        crossed_fingers[message.author] = int(time.time())
        # send message
        ctx.send(f"{message.author} has crossed their fingers! They're immune from the cheese touch for 60 seconds!")

# init command
@bot.command(name='init', aliases=['start', 'begin', 'initialize'])
async def await_init(ctx, arg: discord.User):
    # set the specified user as the initial cheese touch holder
    cheesetouch_holder = arg
    # send message
    ctx.send(f"Let the games begin... {cheesetouch_holder} is the first cheese-touch holder!")

# TODO help command




# run the bot
bot.run(TOKEN.strip())