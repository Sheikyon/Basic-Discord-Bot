import discord # Import discord.py dependency
from discord.ext import commands # Importing the commands
import datetime 

print("Basic bot written in less than 4 minutes. \nWritted by Sheikyon (https://github.com/Sheikyon)") # I guess you already know the utility of print(), right?

bot = commands.Bot(command_prefix='#', description="That's a test bot.") # Define "#" as a prefix for commands.


# Hello and Goodbye

@bot.command()
async def hello(ctx):
     await ctx.send('Goodbye') # Type "#hello" for the bot to reply "Goodbye"

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="write #hello")) # Set a state that says "write #hello"
    print('The bot is ready')

bot.run('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz') # Put your bot token here
