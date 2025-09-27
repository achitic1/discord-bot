import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
from datetime import datetime
import os
import logging
import random

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is here bros')
    daily_message.start()

def get_random_member(guild):
    #Filter out bots and get only human members
    human_members = [member for member in guild.members if not member.bot]

    if human_members:
        return random.choice(human_members)
    return None

@tasks.loop(hours=24)
async def daily_message():
    for guild in bot.guilds:
        channel = discord.utils.get(guild.text_channels, name='general')
        if not channel:
            channel = next((ch for ch in guild.text_channels
                            if ch.permissions_for(guild.me).send_messages), None)
            
        if channel:
            random_member = get_random_member(guild)

            if random_member:
                await channel.send(f"Shower check {random_member.mention}!")
                print(f"Sent daily message to {guild.name}, mentioned {random_member.display_name}")

@daily_message.before_loop
async def before_daily_message():
    await bot.wait_until_ready()

@bot.event 
async def on_member_join(member):
    await member.send(f'Welcome to the server bro')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f'Hi, how are ya')

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send("You know who else pings?")

# Enter token from .env here
bot.run(token, log_handler=handler, log_level=logging.DEBUG)