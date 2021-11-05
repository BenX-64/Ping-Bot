import discord
from discord.ext import commands
from discord.ext.commands import has_guild_permissions, has_permissions

import os
import sys
import string

from dotenv import load_dotenv
load_dotenv()

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_message(ctx):
    await bot.process_commands(ctx)
    if bot.user == ctx.author: return
    if str(ctx.content).find('@everyone')!=-1 or str(ctx.content).find('@here')!=-1:
        await ctx.channel.send(f'Shut the fuck up {ctx.author.mention}')

bot.run(os.getenv('TOKEN'))
