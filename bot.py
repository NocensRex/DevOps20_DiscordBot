# bot.py
import os

from discord.ext import commands
from dotenv import load_dotenv
import schedule

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.command(name='next', help='Visar vad nästa lektion är och när den börjar.')
async def next_lesson(ctx):
    next_ = schedule.next_lesson()
    await ctx.send(next_)

@bot.command(name='today', help='Visar dagens schema.')
async def lesson_today(ctx):
    today_list = schedule.this_day()
    for item in today_list:
        await ctx.send(item)

bot.run(TOKEN)