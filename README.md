# Cheese Touch Bot
This bot adds a simple cheese touch game to your Discord server!

![Example of Cheese Touch Bot in action!](https://github.com/ethanrasmussen/cheese-touch-bot/blob/master/cheesetouch.PNG)

## To add to your server:
Within `assets.py` enter your bot token and (optionally) the initial cheese-touch holder. The initial cheese-touch holder can be left as `None`. If this is the case, then you'll need to use the `ct init [user]` command.

## TODO List:
* Update poke command to ensure the poked user is on the server & isn't a bot

## Commands:
All commands can be used with any of the following prefixes: 'cheesetouch', 'cheese', or 'ct'. These prefixes are not case sensitive. In the following examples, 'ct' will be used for brevity.
### `ct poke [user]` (or: `ct touch [user]`)
Passes the cheese touch along to someone else!
### `ct cross` (or: `ct crossfingers`)
Crosses your fingers, protecting you from the cheese touch for 60 seconds!
### `ct whois` (or: `ct who`)
Displays the current holder of the cheese touch.
### `ct init [user]` (or: `ct start [user]` or `ct begin [user]`)
Select an initial user to be the cheese-touch holder, if not specified within `assets.py`.
### `ct help` (or: `ct info`)
Displays a list of all the bot's commands.
