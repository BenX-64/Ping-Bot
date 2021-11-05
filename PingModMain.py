import discord
from discord.ext import commands
import os
import sys
import string

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_message(ctx):
    if bot.user == ctx.author: return

    if str(ctx.content).find(f'<@!{bot.user.id}>')!=-1:
        await ctx.channel.send(f'FUCK YOU {ctx.author.mention}')
        
    elif str(ctx.content).find('@everyone')!=-1 or str(ctx.content).find('@here')!=-1:
        await ctx.channel.send(f'Shut the fuck up {ctx.author.mention}')
        

bot.run(os.getenv('TOKEN'))
