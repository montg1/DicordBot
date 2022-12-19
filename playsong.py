import discord
from discord.ext import commands
from google.oauth2.credentials import Credentials
import googleapiclient.discovery
import pafy

# Replace TOKEN with your bot's token
TOKEN = ''

# Replace API_KEY with your YouTube API key
API_KEY = 'AIzaSyCKeOz2tlYLp0-JyxwVKonowW74kjwn2Lc'

# Create a Discord client
client = commands.Bot(intents=discord.Intents.all() , command_prefix= "!" , description='The Best Bot For the Best User!')


@client.event
async def on_message(message):
    # Check if the message is a command to join a voice channel
    if message.content.startswith('!join'):
        # Get the voice channel to join
        voice_channel = message.author.voice.channel
        if voice_channel is not None:
            # Join the voice channel
            await voice_channel.connect()
        else:
            # Send a message if the user is not in a voice channel
            await message.channel.send('You are not in a voice channel!')
    # Check if the message is a command to leave a voice channel
    elif message.content.startswith('!leave'):
        # Get the voice channel to leave
        voice_client = message.guild.voice_client
        if voice_client is not None:
            # Leave the voice channel
            await voice_client.disconnect()
        else:
            # Send a message if the user is not in a voice channel
            await message.channel.send('You are not in a voice channel!')
    # Check if the message is a command to play a YouTube video
    elif message.content.startswith('!play'):
        # Get the query from the command
        query = message.content.split(' ', 1)[1]
        # Create a YouTube API service
        youtube = googleapiclient.discovery.build(
            'youtube', 'v3', developerKey
            =API_KEY)
        # Search for a video
        search_response = youtube.search().list(
            part='id,snippet',
            q=query,
            type='video',
            maxResults=1
        ).execute()
        # Get the video ID
        video_id = search_response['items'][0]['id']['videoId']
        # Send the video ID to the voice channel
        await message.channel.send(f'https://www.youtube.com/watch?v={video_id}')
        # Get the voice channel to play the video in
        voice_client = message.guild.voice_client
        if voice_client is not None:
            # Play the video
            print('Playing video')
            voice_client.play(discord.FFmpegPCMAudio(f'https://www.youtube.com/watch?v={video_id}'))
        else:
            # Send a message if the user is not in a voice channel
            await message.channel.send('You are not in a voice channel!')
@client.command()
async def greet(ctx):
    await ctx.send("Hello, World!")


# Run the client on the server
client.run(TOKEN)
