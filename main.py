
import discord
import os
import requests
import json
import random

# Create an Intents object to specify the events the bot will listen to
intents = discord.Intents.default()
intents.message_content = True

# Create the Discord client, passing the intents object
client = discord.Client(intents=intents)


# Two Lists containing keywords
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person!"
]

# Function that returns a zen quote using an API
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  
  json_data = json.loads(response.text)
  quote = '"' + json_data[0]['q'] + '" - ' + json_data[0]['a']
  
  return quote


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

  if msg.startswith("%"):
    if msg == "%hello":
      await message.channel.send("Hello there!")

    if msg == "%inspire":
      quote = get_quote()
      await message.channel.send(quote)


client.run("[TOKEN]")
