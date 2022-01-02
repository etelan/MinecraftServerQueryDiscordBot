import requests
import os
from dotenv import load_dotenv

# Load environmental variables
load_dotenv()
BOTTOKEN = os.getenv('DISCORD_BOT_TOKEN')
APPID = os.getenv('DISCORD_APP_ID')

# Setup our url
url = "https://discord.com/api/v8/applications/" + APPID + "/commands"

# This is an example CHAT_INPUT or Slash Command, with a type of 1
jsonPlayers = {
    "name": "players",
    "type": 1,
    "description": "Shows who is online!",
    "options": []
}

jsonPing = {
    "name": "ping",
    "type": 1,
    "description": "Checks the latency of the minecraft server.",
    "options": []
}

# For authorization, you can use either your bot token
headers = {
    "Authorization": "Bot " + BOTTOKEN
}

r = requests.post(url, headers=headers, json=jsonPlayers)
r = requests.post(url, headers=headers, json=jsonPing)


print("Done.")
