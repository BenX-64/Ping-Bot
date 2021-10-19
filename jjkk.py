import discord
from discord.ext import commands


intents = discord.Intents.all()

bot = commands.Bot(command_prefix=".", intents=intents)


@bot.event
async def on_ready():
    print(f"Bot is ready")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="example"))

@bot.event
async def on_message(message):
    forbidden_word = "word"
    if forbidden_word in message.content:
        await message.delete()

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member):
    await member.kick()
    await ctx.send(f"Member {member} has been kicked")


bot.run("ODk5NTY0MTc1NTY5ODYyNjk2.YW0mbA.7POogOHFh9ZmyW8UF53cYSDz4MI")