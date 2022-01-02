# Minecraft Server Query Discord Bot

This is a simple discord bot, that queries the Minecraft server to check the following.

* Players Online
* Ping Time
* Server Offline / Online / Refusing Connections

## Installation

Download [python3](https://www.python.org/downloads/), and click `Add Python 3. x to PATH` when installing.

### Requirements
Use the package manager [pip3](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
pip3 install -r /[where-you-unzipped-it]/MinecraftServerQueryDiscordBot/requirements.txt
```

Alternatively, you can manually install the requirements.
```bash
pip3 install python-dotenv
pip3 install discord-py-slash-command
pip3 install discord.py
pip3 install mcstatus
```

### Make your discord bot token
1. [Discord Developer Portal](https://discord.com/developers/).

2. New Application, fill out the name.

3. Bot Tab. Add Bot. 

4. Click to Reveal Token.

5. Tick all the intents (Privileged Gateway Intents). These are...

- Presence Intent
- Server Members Intent
- Message Content Intent

### Setup `.env` File
Make a file in the same directory as the python script titled .env.

The application id can found under the General Information, then Application Id.

Grab your discord tokens, and fill out your env file as follows.

#### Template `.env`
```
DISCORD_BOT_TOKEN=[your bot token]
DISCORD_APP_ID=[your app id]
MINECRAFT_IP=[Your Server IP]
```

#### Example `.env`
```
DISCORD_BOT_TOKEN=OTI3MzA0NDc2NTI2NzcyMjI0.YdIRlw.Wh_XsMqNELhc1kAPo2kM903kJpl
DISCORD_APP_ID=927304276526772229
MINECRAFT_IP=133.114.63.200:25565
```

## Usage

Just run the file, by double clicking `MinecraftServerQueryDiscordBot.py`.

To add the discord bot to your server, click the OAuth2 tab of your application.

Then, click URL Generator.

#### Scopes
```
applications.commands
bot
```

#### Permissions
```
Send Messages
Use Slash Commands
```

Copy and paste the url into your search bar and the rest is self explanatory.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

For any other questions, feel free to send me an email on `minecraftbot@alexisbaker.uk
`

## License
[MIT](https://choosealicense.com/licenses/mit/)
