from mcstatus import MinecraftServer
import os
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from dotenv import load_dotenv

load_dotenv()

# These will never change
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
IP = os.getenv('MINECRAFT_IP')

# Setup the bot
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
slash = SlashCommand(bot)

# Commands
@slash.slash(name="ping")
async def _test(ctx: SlashContext):
    await ctx.defer()
    # Connect
    server = MinecraftServer.lookup(str(IP))

    # Ping
    response = ""
    try:
        latency = server.ping()
        response = f"The server replied in {latency} ms"
    except TimeoutError:
        response = "🦀 Server is dead 🦀"
    except ConnectionRefusedError:
        response = "Server is refusing connections at this time.\nPlease try again later."
                    
    await ctx.send(response)

@slash.slash(name="players")
async def _test(ctx: SlashContext):
    await ctx.defer()
    # Connect
    server = MinecraftServer.lookup(str(IP))

    # Player Query
    try:
        query = server.query()
        if query.players.names :
            response = f"The server has the following players online: {', '.join(query.players.names)}"
        else:
            response =  "Server is empty | No players online"
    except TimeoutError:
        response = "🦀 Server is dead 🦀"
    except ConnectionRefusedError:
        response = "Server is refusing connections at this time.\nPlease try again later."
    
                
    await ctx.send(response)

# Run the bot
bot.run(TOKEN)
