# Cheese Touch Bot
This bot adds a simple cheese touch game to your Discord server!

![Example of Cheese Touch Bot in action!](https://github.com/ethanrasmussen/cheese-touch-bot/blob/master/cheesetouch.PNG)

## To add to your server:
Create a new file 'assets.py' containing 2 variables called 'token' and 'guild_id', which represent the bot token and server/guild ID respectively (these should be string values).

## TODO List:
* Clean up junk code from bot.py (particularly deprecated & unused code)
* Update poke command to ensure the poked user is on the server & isn't a bot
* Either remove init command, or fix it

## Commands:
All commands can be used with any of the following prefixes: 'cheesetouch', 'cheese', or 'ct'. These prefixes are not case sensitive. In the following examples, 'ct' will be used for brevity.
### ct poke [user] (or: ct touch [user])
Passes the cheese touch along to someone else!
### ct cross (or: ct crossfingers)
Crosses your fingers, protecting you from the cheese touch for 60 seconds!
### ct whois (or: ct who)
Displays the current holder of the cheese touch.
### ct help (or: ct info)
Displays a list of all the bot's commands.
