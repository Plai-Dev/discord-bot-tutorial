import discord
from discord.ext import commands

with open('token.txt', 'r') as token_file:
    token = token_file.readline()

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='.', intents=intents)

# commands
@bot.command()
async def echo(ctx: commands.Context, *msg):
    await ctx.send(' '.join(msg))

bot.run(token)
