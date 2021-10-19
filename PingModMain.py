from logging import _Level
import discord
from discord.ext import commands
from discord.ext.commands import has_guild_permissions, has_permissions

import os
import sys
import string

from dotenv import load_dotenv
load_dotenv()

global mode
global hostility
global tolerance

mode = 0
hostility = 1
tolerance = 5

bot = commands.Bot(command_prefix = '!')
'''
@bot.event
async def on_message(ctx):
    if bot.user == ctx.author: return
    await ctx.channel.send('test')
'''

@bot.command()
@has_permissions(administrator = True)
async def config(ctx, setting, level):
    global tolerance
    global hostility
    global mode
    if str(setting) == "mode":
        await ctx.reply(f'Changing {setting} level from {mode} to {level}')
        mode = level
    elif str(setting) == "hostility":
        await ctx.reply(f'Changing {setting} level from {hostility} to {level}')
        hostility = level
    elif str(setting) == "tolerance":
        await ctx.reply(f'Changing {setting} level from {tolerance} to {level}')
        tolerance = level

@bot.event
async def on_message(ctx):
    await bot.process_commands(ctx)
    if bot.user == ctx.author: return
    print("t")
    
bot.run(os.getenv('TOKEN'))
