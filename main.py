
import discord
import random
from discord.ext import commands
from config import TOKEN
from utils import get_quote, sad_words, starter_encouragements

# Create an Intents object to specify the events the bot will listen to
intents = discord.Intents.default()
intents.message_content = True

# Create the Discord bot, defining its command prefix and passing the intents object
bot = commands.Bot(command_prefix='%', intents=intents)

# Start Up Console Message
@bot.event
async def on_ready():
  print(f"We have logged in as {bot.user}")

# Main Segment
@bot.command()
async def ping(ctx):
  await ctx.send("pong")

@bot.command()
async def hello(ctx):
  await ctx.send("Hello there!")

@bot.command()
async def inspire(ctx):
  quote = get_quote()
  await ctx.send(quote)

bot.run(TOKEN)
