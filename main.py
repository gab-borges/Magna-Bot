
import os
import discord
import random
from config import TOKEN
from utils import get_quote, sad_words, starter_encouragements

# Create an Intents object to specify the events the bot will listen to
intents = discord.Intents.default()
intents.message_content = True

# Create the Discord client, passing the intents object
client = discord.Client(intents=intents)

# Start Up Console Message
@client.event
async def on_ready():
  print(f"We have logged in as {client.user}")

# Main Segment
@client.event
async def on_message(message):
  msg = message.content
  
  if message.author == client.user:
    return

  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

  # Message with the prefix:
  if msg.startswith("%"):
    if msg == "%hello":
      await message.channel.send("Hello there!")

    if msg == "%inspire":
      quote = get_quote()
      await message.channel.send(quote)


client.run(TOKEN)
