#!/usr/bin/env python

import os
import discord
from datetime import datetime
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

################################################################################

intents = discord.Intents().all() # Set up permissions in Discord portal
bot = commands.Bot(command_prefix='>', description="My bot", intents=intents)

### Commands ###

@bot.command()
async def ping(context):
    await context.send('pong')

@bot.command()
async def time(context):
    await context.send(str(datetime.now()))

################################################################################

bot.run(DISCORD_BOT_TOKEN)