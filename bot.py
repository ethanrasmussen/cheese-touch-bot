from discord.ext import commands
import discord
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

# initialize CT holder w/ 'None' value
cheesetouch_holder: discord.User = None

# initialize dictionary of users crossing fingers
# FORMAT: discord.User : Timestamp of last time fingers crossed (unix style)

# poke command
# TODO: account for 2 scenarios: pokee has fingers crossed; and pokee not in server
@bot.command(name='poke', aliases=['touch'])
async def await_poke(message, ctx, arg: discord.User):
    # check if message sender is the current cheesetouch holder
    if str(message.author.id) == str(cheesetouch_holder.id):
        arg = arg.replace("<", "")
        arg = arg.replace(">", "")
        arg = arg.replace("@", "")
        cheesetouch_holder = str(arg.id)
        ctx.send(f"{message.author} passed the cheese-touch to {cheesetouch_holder}!")
    else:
        ctx.send(f"Hey {message.author}! You can't do that! You don't have the cheese touch!")

# whois command
@bot.command(name='whois', aliases=['who is'])
async def await_whois(ctx):
    ctx.send(f"Currently, {cheesetouch_holder} has the cheese touch!")

# TODO cross command

# TODO init command

# TODO help command




# run the bot
bot.run(TOKEN.strip())