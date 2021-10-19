import discord
from discord.ext import commands
from discord.ext.commands import has_guild_permissions, has_permissions

import os
import sys
import string

from dotenv import load_dotenv
load_dotenv()

from serverconfig import serverconfig

bot = commands.Bot(command_prefix = '!')
activeconfig = serverconfig(0, 1, 5)


@bot.command()
@has_permissions(administrator = True)
async def config(ctx, setting, level):
    if str(setting) == "mode":
        await ctx.reply(f'Changing {setting} level from {activeconfig.mode} to {level}')
        activeconfig.setMode(level)
    elif str(setting) == "hostility":
        await ctx.reply(f'Changing {setting} level from {activeconfig.hostility} to {level}')
        activeconfig.setHostility(level)
    elif str(setting) == "maxwarnings":
        await ctx.reply(f'Changing {setting} level from {activeconfig.maxwarnings} to {level}')
        activeconfig.setMaxwarnings(level)
    else: await ctx.reply('Error: Invalid Setting, Only "mode" (0-2), "hostility" (1-3), "maxwarnings" (0+) are valid arguments. ')

@bot.event
async def on_message(ctx):
    await bot.process_commands(ctx)
    if bot.user == ctx.author: return
    if str(ctx.content).find('@everyone')!=-1 or str(ctx.content).find('@here')!=-1:
        await ctx.channel.send("SHUT UP")
    #print(ctx.author.id)

bot.run(os.getenv('TOKEN'))
