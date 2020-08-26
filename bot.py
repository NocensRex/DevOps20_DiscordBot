# bot.py
import os
import random

import discord
from dotenv import load_dotenv
from datetime import date
import schedule

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'next!':
        await message.channel.send(schedule.next_lesson())

    if message.content == 'today!':
        items = schedule.this_day()
        for item in items:
            await message.channel.send(item)

client.run(TOKEN)

