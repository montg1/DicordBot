from matplotlib import animation
import openai
import discord
from discord.ext import commands
bot = commands.Bot(intents=discord.Intents.all() , command_prefix= "!" , description='The Best Bot For the Best User!')
openai.api_key = "API_KEY"


@bot.command()
async def greet(ctx):
    await ctx.send("Hello, World!")
    
@bot.command()
async def pi(ctx):
    await ctx.send("3.141")

@bot.command()
async def ping(ctx):
    await ctx.channel.send("pong")

@bot.command()
async def find(ctx, *args):
    message = ""
    for arg in args:
        message = message + " " + arg
    prompt = (f"{message}")
    model_engine = "text-davinci-002"
    prompt = (f"{message}")
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completions.choices[0].text
    await ctx.channel.send(response)

bot.run("DISCORD_TOKEN")
