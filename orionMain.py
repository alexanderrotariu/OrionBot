import discord
import requests
import os
from dotenv import load_dotenv

#CREDENTIALS
load_dotenv('.env')

client = discord.Client()

@client.event
async def on_ready():
    print('incredible. we logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

#if the emoji incredible is sent somewhere, resend that emoji
    if '<:incredible:938820326761058374>' in message.content:
        await message.channel.send('<:incredible:938820326761058374>')  

client.run(os.getenv('TOKEN'))