import discord
from discord.ext import commands
import asyncio
import os
import sys
import string

bot = commands.Bot(command_prefix = '!')
target = 899821011199991818

#Timed mute this format: 1d, 20s, 30m, etc..
#@bot.command(aliases=['tempmute'])
#@commands.has_permission(manage_messages=True)
async def mute(ctx, member: discord.Member=None, time=None, *, reason=None):
    if not member:
        print("No member")
        #await ctx.send("You must mention a member to mute!")
    elif not time:
        print("no time")
        #await ctx.send("You must mention a time!")
    else:
        if not reason:
            reason="No reason given"
        #Now timed mute manipulation
        try:
            seconds = time
        except Exception as e:
            print(e)
            print("no time input")
            #await ctx.send("Invalid time input")
            return
        Muted = discord.utils.get(ctx.guild.roles, name="Muted")
        if not Muted:
            Muted = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.channels:
                await channel.set_permissions(Muted, speak=False, send_messages=False, read_message_history=True, read_messages=False)
        await member.add_roles(Muted, reason=reason)
        muted_embed = discord.Embed(title="Muted a user", description=f"{member.mention} Was muted by {ctx.author.mention} for {reason} to {time}")
       # await ctx.send(embed=muted_embed)
        await asyncio.sleep(seconds)
        await member.remove_roles(Muted)
        unmute_embed = discord.Embed(title="Mute over!", description=(f'{ctx.author.mention} muted to {member.mention} for {reason} is over after {time}'))
       # await ctx.send(embed=unmute_embed)


@bot.event
async def on_message(ctx):
    if bot.user == ctx.author: return
    if str(ctx.content).find(f'<@!{bot.user.id}>')!=-1:
        await ctx.channel.send(f'FUCK YOU {ctx.author.mention}')
    elif str(ctx.content).find('@everyone')!=-1 or str(ctx.content).find('@here')!=-1:
        await ctx.channel.send(f'Shut the fuck up {ctx.author.mention}')
        
        if(ctx.author.id == target):
            if ctx.guild.fetch_member(target) is not None:
                await ctx.guild.fetch_member(target).edit(mute = True)
            #await mute(ctx.guild.get_member(target), 10, "shut up")
            
            
bot.run("ODk5NTY0MTc1NTY5ODYyNjk2.YW0mbA.3gjTVgblx8keAMtTrRyW4Pf3obY")