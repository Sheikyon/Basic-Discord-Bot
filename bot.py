import discord # Import discord.py dependency
from discord.ext import commands # Importing the commands
import datetime 

print("Basic bot written in less than 4 minutes. \nWritted by Sheikyon (https://github.com/Sheikyon)")

bot = commands.Bot(command_prefix='#', description="That's a test bot.")


# Hello and Goodbye

@bot.command()
async def hello(ctx):
     await ctx.send('Goodbye')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="write #hello"))
    print('The bot is ready')

bot.run('zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz') # Put your bot token here