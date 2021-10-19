import discord
from discord.ext import commands
from discord.ext.commands import has_guild_permissions, has_permissions
import os
import sys
import string
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix = '!')

@bot.command()
@has_permissions(administrator = True)
async def config(ctx, setting, level):
    await ctx.reply('Changing hostility level from' )

    
bot.run(os.getenv('TOKEN'))
