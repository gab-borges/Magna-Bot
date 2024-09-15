
import requests
import json

def get_quote():
  """
  Function that returns a zen quote using an API
  """
  response = requests.get("https://zenquotes.io/api/random")
  
  json_data = json.loads(response.text)
  quote = '"' + json_data[0]['q'] + '" - ' + json_data[0]['a']
  
  return quote

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starter_encouragements = [
    "Cheer up!",
    "Hang in there.",
    "You are a great person!"
]
