
import json
import requests

def get_quote():
  """
  Function that returns a zen quote using an API
  """
  response = requests.get("https://zenquotes.io/api/random")
  
  json_data = json.loads(response.text)
  quote = '"' + json_data[0]['q'] + '" - ' + json_data[0]['a']
  
  return quote

def get_joke():
  """
  Function that returns a joke with a setup and punchline using an API
  """
  response = requests.get("https://official-joke-api.appspot.com/random_joke")
  joke_data = response.json()
  setup = joke_data['setup']
  punchline = joke_data['punchline']

  joke = f"{setup}\n||{punchline}||"
  return joke


sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = [
    "Cheer up!",
    "Hang in there.",
    "You are a great person!"
]
