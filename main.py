import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix='%')

@client.command()
async def load(context, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(context, extension):
    client.unload_extension(f'cogs.{extension}')


client.load_extension(f'cogs.bot')
client.run(TOKEN)
