# basic dependencies
import time
from assets import token, guild_id, initial_ctholder
# discord.py dependencies
from discord.ext import commands
import discord

# discord bot token & guild ID (server ID)
TOKEN = token
GUILDID = guild_id # TODO: actually utilize this var
INITIAL_CHEESETOUCH_HOLDER = initial_ctholder

# init bot
bot = commands.Bot(command_prefix=('cheesetouch ', 'cheese ', 'Cheese ', 'Cheesetouch ', 'ct ', 'CT '), case_insensitive=True, help_command=None)
guild = bot.get_guild(GUILDID) # TODO: implement this

# when bot online
@bot.event
async def on_ready():
    # console output
    print('Bot online.')
    print(f'Name: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    # set status
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='Cheese Touch'))

# parse every msg for cmds
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

# initialize CT holder w/ 'None' value, unless an initial value is specified
cheesetouch_holder = None
if INITIAL_CHEESETOUCH_HOLDER != None:
    cheesetouch_holder = INITIAL_CHEESETOUCH_HOLDER

# initialize dictionary of users crossing fingers
# FORMAT: discord.User : Timestamp of last time fingers crossed (unix style)
crossed_fingers = dict()

# poke command
# accounts for 2 scenarios: pokee has fingers crossed; and pokee not in server
@bot.command(name='poke', aliases=['touch'])
async def await_poke(ctx, arg: discord.User):
    global cheesetouch_holder
    # check if message sender is the current cheesetouch holder
    if str(ctx.author) == cheesetouch_holder:
        # TODO: check if user is in server?
        finger_timestamp = crossed_fingers.get(arg)
        if finger_timestamp == None:
            finger_timestamp = 0
        # if time since fingers crossed is 60s or less, they're safe
        if int(time.time()) - finger_timestamp <= 60:
            await ctx.send(f"Nice try! But {arg} still has their fingers crossed!")
        # else, they're the new cheesetouch holder!
        else:
            cheesetouch_holder = arg
            await ctx.send(f"{ctx.author} passed the cheese-touch to {cheesetouch_holder}!")
    else:
        await ctx.send(f"Hey {ctx.author}! You can't do that! You don't have the cheese touch!")

# whois command
@bot.command(name='whois', aliases=['who'])
async def await_whois(ctx):
    global cheesetouch_holder
    await ctx.send(f"Currently, {cheesetouch_holder} has the cheese touch!")

# cross command
@bot.command(name='cross', aliases=['crossfingers'])
async def await_cross(ctx):
    global cheesetouch_holder
    # if user is the cheese touch holder, mock them
    if str(ctx.author) == cheesetouch_holder:
        await ctx.send(f"Really {ctx.author}? Nice try... but you already have the cheese touch!")
    # else, cross their fingers
    else:
        # add author to dictionary of crossed fingers
        crossed_fingers[ctx.author] = int(time.time())
        # send message
        await ctx.send(f"{ctx.author} has crossed their fingers! They're immune from the cheese touch for 60 seconds!")

# init command
@bot.command(name='init', aliases=['start', 'begin', 'initialize'])
async def await_init(ctx, user: discord.User):
    global cheesetouch_holder
    # allow command if there is no CT holder
    if cheesetouch_holder == None:
        # set the specified user as the initial cheese touch holder
        cheesetouch_holder = user
        # send message
        await ctx.send(f"Let the games begin... {cheesetouch_holder} is the first cheese-touch holder!")
    else:
        await ctx.send(f"C'mon man... You can't do that! {cheesetouch_holder} already has the cheese-touch!")

# help command
@bot.command(name='help', aliases=['info'])
async def await_help(ctx):
    desc = 'To use commands: cheesetouch [command] [args]\n' \
           'ct poke [user]: Passes the cheese-touch\n' \
           'ct whois: Tells who the current cheese-touch holder is\n' \
           'ct cross: Cross your fingers for 60 seconds\n' \
           'ct init [user]: Starts the game initially (DEPRECATED)'
    embed = discord.Embed(title='Help', description=desc, url="https://github.com/ethanrasmussen/cheese-touch-bot")
    await ctx.send(embed=embed)

# run the bot
bot.run(TOKEN.strip())