
import discord
from discord.ext import commands
bot = commands.Bot(intents=discord.Intents.all() , command_prefix= "!" , description='The Best Bot For the Best User!')



@bot.command()
async def greet(ctx):
    await ctx.send("Hello, World!")
    
@bot.command()
async def pi(ctx):
    await ctx.send("3.141")

bot.run("TOKEN")
