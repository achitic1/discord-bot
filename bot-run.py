import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix='!', intents=discord.Intents.default())

@bot.event

async def on_ready():
    print(f'{bot.user} is here bros')

@bot.commmand(name='hello')
async def hello(ctx):
    await ctx.send(f'Hi, how are ya')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send("You know who else pings?")

# Enter token from .env here
bot.run(os.getenv('DISCORD_TOKEN'))