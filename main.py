import sys
import traceback

import discord
from discord.ext import commands
import os

TOKEN = 'MTA5NTA2ODk5Mjg1MjQ1OTU3MA.GjFa7p.o_YGjdns3tUW0Ejyql1-n6pUU1bMvnbfI7mQEY'
intents = discord.Intents.all()


class MusicBot(commands.Bot):
    initial_extensions = ['cogs.playcommand']

    async def on_ready(self):
        print('Music online!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
        await self.process_commands(message)


##################################################

client = MusicBot(command_prefix='!', intents=intents)


async def load_extensions():
    for extension in client.initial_extensions:
        await client.load_extension()


client.run(TOKEN)
