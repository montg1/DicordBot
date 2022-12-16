
import discord
from discord.ext import commands
bot = commands.Bot(intents=discord.Intents.all() , command_prefix= "!" , description='The Best Bot For the Best User!')



@bot.command()
async def greet(ctx):
    await ctx.send("Hello, World!")

async def pi(ctx):
    await ctx.send("3.141")

bot.run("MTA1MzI2NjA5NjA3NTA2MzM0Ng.G95O8N.baMEa0jQrn4aARYSxH1cFUSKl0b_8JDbz8Voqk")
