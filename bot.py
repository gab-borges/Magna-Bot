
import discord
from discord.ext import commands
from config import TOKEN, OPENAI_API_KEY
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='%', intents=intents)

# Load all commands from the commands folder
for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')

# Load all event handlers from the events folder
for filename in os.listdir('./events'):
    if filename.endswith('.py'):
        bot.load_extension(f'events.{filename[:-3]}')

bot.run(TOKEN)
